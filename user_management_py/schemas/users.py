"""
Fastapi Poetry Boilerplate.

A boilerplate for fastapi python project supported by poetry.
"""

from pydantic import BaseModel, Field
from user_management_py.models.users import UserCreate, UserRead


class CreateUserRequest(UserCreate):
    """Docstring."""
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
