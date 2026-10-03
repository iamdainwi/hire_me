import uuid
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator


class _EmailMixin(BaseModel):
    email: EmailStr

    @field_validator("email")
    @classmethod
    def normalize_email(cls, v: str) -> str:
        return v.strip().lower()


class RegisterRequest(_EmailMixin):
    password: str = Field(min_length=8, max_length=72)  # bcrypt 72-byte limit
    full_name: str | None = Field(default=None, max_length=120)
    role: Literal["student", "company", "mentor"]  # admin never self-registers
    accept_terms: bool
    ai_processing_consent: bool = False

    @field_validator("accept_terms")
    @classmethod
    def terms_required(cls, v: bool) -> bool:
        if not v:
            raise ValueError("Terms must be accepted")
        return v

    @field_validator("password")
    @classmethod
    def password_strength(cls, v: str) -> str:
        if not any(c.isalpha() for c in v) or not any(c.isdigit() for c in v):
            raise ValueError("Password must contain a letter and a digit")
        if len(v.encode()) > 72:
            raise ValueError("Password too long")
        return v


class LoginRequest(_EmailMixin):
    password: str = Field(min_length=1, max_length=72)


class RefreshRequest(BaseModel):
    refresh_token: str


class VerifyEmailRequest(BaseModel):
    token: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: Literal["bearer"] = "bearer"


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    email: EmailStr
    full_name: str | None
    role: str
    is_verified: bool
    created_at: datetime


class UpdateProfileRequest(BaseModel):
    full_name: str | None = Field(default=None, max_length=120)


class ChangePasswordRequest(BaseModel):
    current_password: str = Field(min_length=1, max_length=72)
    new_password: str = Field(min_length=8, max_length=72)