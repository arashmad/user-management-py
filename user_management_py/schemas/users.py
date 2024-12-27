"""
Fastapi Poetry Boilerplate.

A boilerplate for fastapi python project supported by poetry.
"""

from pydantic import BaseModel, Field
from user_management_py.models.users import UserCreate, UserRead


class CreateUserRequest(UserCreate):
    """Docstring."""
    email: str = Field(
        title="Email",
        description="Email address of the user.")

    password: str = Field(
        title="Password",
        description="Password of the user.")

    firstname: str | None = Field(
        title="Firstname",
        description="User account firstname.",
        default="")

    lastname: str | None = Field(
        title="Lastname",
        description="User account lastname.",
        default="")

    model_config = {
        "json_schema_extra": {
            "title": "Message",
            "example": {
                "email": "john@doe@user.com",
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
