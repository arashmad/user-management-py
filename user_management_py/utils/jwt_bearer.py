"""
Fastapi Poetry Boilerplate.

A boilerplate for fastapi python project supported by poetry.
"""

import jwt
import time
from typing import Dict
from datetime import datetime, timedelta, timezone

from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from user_management_py.crud.User import get_user_by_id

JWT_ALGORITHM = "HS256"

# Helper to get user's unique JWT secret


def jwt_encode(user_id: str, salt: str, expires_delta: timedelta = 15):
    """Docstring."""
    expire = datetime.now(timezone.utc) + expires_delta
    payload = {"user_id": user_id}
    payload.update({"exp": expire})
    encoded_jwt = jwt.encode(payload, salt, algorithm=JWT_ALGORITHM)
    return encoded_jwt


# def jwt_decode(token: str, user_id: str) -> Dict:
#     """Docstring."""
#     try:
#         user = get_user_by_id(user_id=user_id)
#         salt = user.salt_jwt
#         decoded_token = jwt.decode(token, salt, algorithms=[JWT_ALGORITHM])
#         if decoded_token["expires"] < time.time():
#             raise HTTPException(status_code=401, detail="Token has expired.")
#         return decoded_token
#     except jwt.ExpiredSignatureError:
#         raise HTTPException(status_code=401, detail="Token has expired.")
#     except jwt.InvalidTokenError:
#         raise HTTPException(status_code=401, detail="Invalid token.")


class JWTBearer(HTTPBearer):
    """Docstring."""

    def __init__(self, auto_error: bool = True):
        """Docstring."""
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> str:
        """Docstring."""
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if credentials.scheme != "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication scheme.")

            token = credentials.credentials
            # Extract the username from the token (replace with your actual logic)
            try:
                decoded = \
                    jwt.decode(token, options={"verify_signature": False})
                user_id = decoded.get("user_id")
            except:
                raise HTTPException(
                    status_code=403, detail="Invalid token format.")

            if not user_id:
                raise HTTPException(
                    status_code=403, detail="Token content is not valid.")

            # ToDO validate token in signature mode.
            # jwt_decode(token=token, user_id=user_id)

            return user_id
        else:
            raise HTTPException(
                status_code=403, detail="Invalid authorization code.")
