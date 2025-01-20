"""Docstring."""

from sqlmodel import Session, select
from fastapi import Depends

from user_management_py.db.connection import get_session
from user_management_py.models.users import Users


def get_user_by_email(email: str, session: Session = Depends(get_session)) -> Users | None:
    """Retrieve a user by email."""
    return session.exec(select(Users).where(Users.email == email)).first()


def get_user_by_id(user_id: str, session: Session = Depends(get_session)) -> Users | None:
    """Retrieve a user by user_id."""
    return session.exec(select(Users).where(Users.user_id == user_id)).first()
