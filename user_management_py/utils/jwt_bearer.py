"""
Fastapi Poetry Boilerplate.

A boilerplate for fastapi python project supported by poetry.
"""

import time
from typing import Dict, Any
from datetime import datetime, timedelta, timezone

import jwt
from sqlmodel import Session
from fastapi import Request, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from user_management_py.db.connection import get_session
from user_management_py.crud.users import get_user_by_id

JWT_ALGORITHM = "HS256"


def jwt_encode(
        email: str,
        user_id: str,
        salt: str,
        expires_delta: timedelta = timedelta(minutes=15)) -> str:
    """Generate a JWT token with an expiration date."""
    expiration_time = datetime.now(timezone.utc) + expires_delta
    token_payload = {
        "email": email,
        "user_id": user_id,
        "exp": expiration_time}
    return jwt.encode(token_payload, salt, algorithm=JWT_ALGORITHM)


def decode_and_validate_token(token: str, session: Session) -> Dict[str, Any]:
    """
    Decode and validate a JWT token.

    This function retrieves the user's salt from the database and validates
    the token against it. It also checks if the token has expired.
    """
    try:
        # Decode without verifying to extract user_id
        payload = jwt.decode(token, options={"verify_signature": False})

        user_id = payload.get("user_id")

        if not user_id:
            raise HTTPException(
                status_code=401, detail="Token content is invalid")

        # Fetch user and verify token using their salt
        user = get_user_by_id(user_id=user_id, session=session)

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        # Verify the token with the user's salt
        verified_payload = jwt.decode(
            token, user.salt_jwt, algorithms=[JWT_ALGORITHM])

        # Check if token has expired
        if verified_payload["exp"] < time.time():
            raise HTTPException(status_code=401, detail="Token has expired")

        return verified_payload

    except jwt.ExpiredSignatureError as e:
        raise HTTPException(status_code=401, detail="Token has expired") from e

    except jwt.InvalidTokenError as e:
        raise HTTPException(
            status_code=401, detail="Invalid token format") from e


class JWTBearer(HTTPBearer):
    """JWT Authentication class for FastAPI."""

    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request, session: Session = Depends(get_session)) -> str:
        """
        Extract and validate the JWT token from the request header.

        Returns the user_id if the token is valid.
        """
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)

        if not credentials or credentials.scheme.lower() != "bearer":
            raise HTTPException(
                status_code=403, detail="Invalid authentication scheme.")

        token = credentials.credentials

        if not token:
            raise HTTPException(
                status_code=403, detail="Token is missing.")

        decoded_payload = \
            decode_and_validate_token(token=token, session=session)

        if not decoded_payload:
            raise HTTPException(
                status_code=401, detail="Token validation failed.")

        return decoded_payload.get("user_id")
