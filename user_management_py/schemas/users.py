"""
Fastapi Poetry Boilerplate.

A boilerplate for fastapi python project supported by poetry.
"""

from typing import Any
from pydantic import BaseModel, Field, field_validator

from user_management_py.models.users import UserCreate, UserRead

from user_management_py.utils.field_validator import validate_email, validate_password


class CreateUserRequest(UserCreate):
    """Docstring."""

    @field_validator("email")
    @classmethod
    def check_field_email(cls, email: str) -> Any:
        """Check the given email."""
        if not validate_email(email):
            raise ValueError("Invalid email address.")
        return email

    @field_validator("password")
    @classmethod
    def check_field_password(cls, password: str) -> Any:
        """Check the given password."""
        is_valid, message = validate_password(password)
        if not is_valid:
            raise ValueError(message)
        return password

    model_config = {
        "json_schema_extra": {
            "title": "Message",
            "example": {
                "email": "john.doe@user.domain",
                "password": "xxxxxxxxxxxx"
            }
        }
    }


class CreateUserResponse(BaseModel):
    """Docstring."""

    user: UserRead = Field(
        title="User",
        description="Created user.")

    model_config = {
        "json_schema_extra": {
            "title": "Message",
            "example": {
                "user":
                    {
                        "user_id": "",
                        "email": "",
                        "firstname": "",
                        "lastname": "",
                        "created_at": ""
                    }
            }
        }
    }
