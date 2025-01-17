"""
Fastapi Poetry Boilerplate.

A boilerplate for fastapi python project supported by poetry.
"""

from datetime import datetime, timedelta, timezone
import jwt
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(email: str, user_id: str, salt: str, expires_delta: timedelta = 15):
    """Docstring."""
    expire = datetime.now(timezone.utc) + expires_delta
    payload = {"email": email, "user_id": user_id}
    payload.update({"exp": expire})
    encoded_jwt = jwt.encode(payload, salt, algorithm="HS256")

    return encoded_jwt
