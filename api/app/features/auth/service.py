import uuid
from datetime import timedelta

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.security import (
    DUMMY_HASH,
    create_token,
    decode_token,
    hash_password,
    verify_password,
)
from app.features.auth.models import Consent, ConsentType, User, UserRole, UserStatus
from app.features.auth.schemas import (
    ChangePasswordRequest,
    LoginRequest,
    RegisterRequest,
    TokenResponse,
    UpdateProfileRequest,
)

ACCESS, REFRESH, VERIFY = "access", "refresh", "verify_email"


def _unauthorized(detail: str = "Invalid or expired token") -> HTTPException:
    return HTTPException(
        status.HTTP_401_UNAUTHORIZED, detail, headers={"WWW-Authenticate": "Bearer"}
    )


def get_user_by_email(db: Session, email: str) -> User | None:
    return db.scalar(select(User).where(User.email == email))


def get_user_by_id(db: Session, user_id: uuid.UUID) -> User | None:
    return db.get(User, user_id)


def issue_tokens(user: User) -> TokenResponse:
    sub = str(user.id)
    return TokenResponse(
        access_token=create_token(sub, ACCESS, timedelta(minutes=settings.ACCESS_TTL_MIN)),
        refresh_token=create_token(sub, REFRESH, timedelta(days=settings.REFRESH_TTL_DAYS)),
    )


def verification_token(user: User) -> str:
    return create_token(str(user.id), VERIFY, timedelta(hours=settings.VERIFY_TTL_HOURS))


def user_from_token(db: Session, token: str, purpose: str) -> User:
    try:
        payload = decode_token(token, purpose)
        user = get_user_by_id(db, uuid.UUID(payload["sub"]))
    except (ValueError, KeyError):
        raise _unauthorized()
    if user is None or user.status != UserStatus.active:
        raise _unauthorized()
    return user


def register(db: Session, data: RegisterRequest) -> tuple[User, str]:
    user = User(
        email=data.email,
        password_hash=hash_password(data.password),
        full_name=data.full_name,
        role=UserRole(data.role),
    )
    db.add(user)
    try:
        db.flush()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status.HTTP_409_CONFLICT, "Email already registered")

    db.add_all(
        [
            Consent(user_id=user.id, type=ConsentType.terms, granted=True),
            Consent(user_id=user.id, type=ConsentType.privacy, granted=True),
            Consent(
                user_id=user.id,
                type=ConsentType.ai_processing,
                granted=data.ai_processing_consent,
            ),
        ]
    )
    db.commit()
    db.refresh(user)
    return user, verification_token(user)


def login(db: Session, data: LoginRequest) -> TokenResponse:
    user = get_user_by_email(db, data.email)
    # constant-time path: always run bcrypt, even for unknown emails
    password_ok = verify_password(data.password, user.password_hash if user else DUMMY_HASH)
    if user is None or not password_ok:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid email or password")
    if user.status != UserStatus.active:
        raise HTTPException(status.HTTP_403_FORBIDDEN, "Account suspended")
    return issue_tokens(user)


def refresh(db: Session, refresh_token: str) -> TokenResponse:
    user = user_from_token(db, refresh_token, REFRESH)
    return issue_tokens(user)


def verify_email(db: Session, token: str) -> None:
    try:
        user = user_from_token(db, token, VERIFY)
    except HTTPException:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Invalid or expired verification link")
    if not user.is_verified:  # idempotent
        user.is_verified = True
        db.commit()


def update_profile(db: Session, user: User, data: UpdateProfileRequest) -> User:
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(user, field, value)
    db.commit()
    db.refresh(user)
    return user


def change_password(db: Session, user: User, data: ChangePasswordRequest) -> None:
    if not verify_password(data.current_password, user.password_hash):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Current password is incorrect")
    user.password_hash = hash_password(data.new_password)
    db.commit()