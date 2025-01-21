"""Docstring."""

from sqlmodel import Session, select

from user_management_py.models.users import Users


def get_user_by_email(email: str, session: Session) -> Users | None:
    """Retrieve a user by email."""
    return session.exec(select(Users).where(Users.email == email)).first()


def get_user_by_id(user_id: str, session: Session) -> Users | None:
    """Retrieve a user by user_id."""
    return session.exec(select(Users).where(Users.user_id == user_id)).first()
