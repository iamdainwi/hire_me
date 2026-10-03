from fastapi import APIRouter, BackgroundTasks, Depends, status
from sqlalchemy.orm import Session

from app.core.deps import get_db
from app.features.auth import service
from app.features.auth.dependencies import get_current_user
from app.features.auth.models import User
from app.features.auth.schemas import (
    ChangePasswordRequest,
    LoginRequest,
    RefreshRequest,
    RegisterRequest,
    TokenResponse,
    UpdateProfileRequest,
    UserResponse,
    VerifyEmailRequest,
)
from app.integrations.email import send_verification_email

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(data: RegisterRequest, background: BackgroundTasks, db: Session = Depends(get_db)):
    user, token = service.register(db, data)
    background.add_task(send_verification_email, user.email, token)
    return user


@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    return service.login(db, data)


@router.post("/refresh", response_model=TokenResponse)
def refresh(data: RefreshRequest, db: Session = Depends(get_db)):
    return service.refresh(db, data.refresh_token)


@router.post("/verify-email", status_code=status.HTTP_204_NO_CONTENT)
def verify_email(data: VerifyEmailRequest, db: Session = Depends(get_db)):
    service.verify_email(db, data.token)


@router.post("/resend-verification", status_code=status.HTTP_204_NO_CONTENT)
def resend_verification(background: BackgroundTasks, user: User = Depends(get_current_user)):
    if not user.is_verified:
        background.add_task(
            send_verification_email, user.email, service.verification_token(user)
        )


@router.get("/me", response_model=UserResponse)
def me(user: User = Depends(get_current_user)):
    return user


@router.patch("/me", response_model=UserResponse)
def update_me(
    data: UpdateProfileRequest,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return service.update_profile(db, user, data)


@router.post("/change-password", status_code=status.HTTP_204_NO_CONTENT)
def change_password(
    data: ChangePasswordRequest,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    service.change_password(db, user, data)