"""
Fastapi Poetry Boilerplate.

A boilerplate for fastapi python project supported by poetry.
"""

import jwt
import time

from pydantic import BaseModel
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(email: str, user_id: str, salt: str, expires_delta: timedelta = 15):
    """Docstring."""
    expire = datetime.now(timezone.utc) + expires_delta
    payload = {"email": email, "user_id": user_id}
    payload.update({"exp": expire})
    encoded_jwt = jwt.encode(payload, salt, algorithm="HS256")

    return encoded_jwt


# class TokenPayload(BaseModel):
#     """Docstring."""
#     email: str
#     user_id: str
#     exp: int


# def validate_access_tokeb(access_token: str, salt: str) -> TokenPayload | None:
#     """Docstring."""
#     try:
#         decoded_token = jwt.decode(access_token, salt, algorithms=["HS256"])
#         payload = \
#             decoded_token if decoded_token["expires"] >= time.time() else None
#     except:
#         payload = None

#     return payload
