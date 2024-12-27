"""Docstring."""


import uuid
from datetime import datetime, timezone

from sqlmodel import Field, SQLModel


def get_datetime_utc_now() -> datetime:
    """Get current datetime in UTC."""
    utc_now = datetime.now(tz=timezone.utc)
    return utc_now


def generate_user_id(email: str) -> str:
    """Generate unique user id from email."""
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, email))


def generate_salt() -> str:
    """Generate random salt."""
    return str(uuid.uuid4())

# Base Model


class BaseUser(SQLModel):
    """Docstring."""
    email: str = Field(
        title="Email",
        description="Email address of the user.",
        unique=True
    )
    firstname: str | None = Field(
        title="Firstname",
        description="User account firstname.",
        default=""
    )
    lastname: str | None = Field(
        title="Lastname",
        description="User account lastname.",
        default=""
    )


# Request Model
class UserCreate(BaseUser):
    """Docstring."""
    password: str = Field(
        title="Password",
        description="Password of the user."
    )


# Response Model
class UserRead(BaseUser):
    """Docstring."""
    user_id: str = Field(
        title="User ID",
        description="Unique identifier for the user."
    )
    created_at: datetime = Field(
        title="Created At",
        description="Timestamp of when the user was created."
    )


# Database Model
class Users(BaseUser, table=True):
    """Docstring."""
    user_id: str = Field(
        title="User ID",
        description="Unique identifier for the user.",
        primary_key=True,
        default_factory=lambda: ""
    )
    password: str = Field(
        title="Password",
        description="Password of the user."
    )
    salt_jwt: str = Field(
        title="Salt",
        description="Salt for JSON Web Token encryption.",
        default_factory=generate_salt
    )
    salt_pass: str = Field(
        title="Salt",
        description="Salt for password encryption.",
        default_factory=generate_salt
    )
    created_at: datetime = Field(
        title="Created At",
        description="Timestamp of when the user was created.",
        default_factory=get_datetime_utc_now
    )
    update_at: datetime | None = Field(
        title="Modified At",
        description="Timestamp of when the user was modified.",
        default=None
    )
    deleted_at: datetime | None = Field(
        title="Deleted At",
        description="Timestamp of when the user was deleted.",
        default=None
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.user_id and self.email:
            self.user_id = generate_user_id(self.email)

    def to_dict(self, exclude_none: bool = False) -> dict:
        """
        Convert the model instance to a dictionary.

        :param exclude_none: Exclude fields with None values if True.
        :return: Dictionary representation of the instance.
        """
        model_dict = self.model_dump(exclude_none=exclude_none)

        for key, value in model_dict.items():
            print(key, value)
            if isinstance(value, datetime):
                model_dict[key] = value.isoformat()

        return model_dict
