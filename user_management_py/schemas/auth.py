"""
User Management System.

Schemas for /auth endpoints
"""

from typing import Any
from pydantic import BaseModel, Field, field_validator

from user_management_py.utils.field_validator import validate_email, validate_password


class LoginRequest(BaseModel):
    """Docstring."""

    email: str = Field(
        title="Email",
        description="Email address of the user.",
        examples=["john@doe@user.com"])

    password: str = Field(
        title="Password",
        description="Password of the user. \
            It must have at least 8 and at most 32 characters and a be a combination of \
            lowercase letter, uppercase letter, digit and special character.",
        examples=["My-Password1"])

    @field_validator("email", mode="before")
    @classmethod
    def check_field_email(cls, email: str) -> Any:
        """Check the given email."""
        if not validate_email(email):
            raise ValueError("Invalid email address.")
        return email

    @field_validator("password", mode="before")
    @classmethod
    def check_field_password(cls, password: str) -> Any:
        """Check the given password."""
        is_valid, message = validate_password(password)
        if not is_valid:
            raise ValueError(message)
        return password

    model_config = {
        "json_schema_extra": {
            "title": "Login Request",
            "example": {
                "email": "john@doe@user.com",
                "password": "xxxxxxxxxxxx"
            }
        }
    }


class LoginResponse(BaseModel):
    """Docstring."""

    access_token: str = Field("Access Token", description="Access Token")
    refresh_token: str = Field("Refresh Token", description="Refresh Token")

    model_config = {
        "json_schema_extra": {
            "title": "Login Response",
            "example": {
                "access_token": "",
                "refresh_token": "",
            }
        }
    }
