"""
Fastapi Poetry Boilerplate.

A boilerplate for fastapi python project supported by poetry.
"""

from sqlmodel import Session, select
from datetime import timedelta

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from user_management_py.db.connection import get_session
from user_management_py.crud import User as user_crud
from user_management_py.utils.jwt_bearer import jwt_encode
from user_management_py.utils.auth import pwd_context

import user_management_py.schemas.general as general_schema
import user_management_py.schemas.auth as auth_schema

router = APIRouter(tags=["Authentication"], prefix="/auth")


@router.post("/login",
             summary="Login user",
             responses={
                 200: {"model": general_schema.Message},
                 401: {"model": general_schema.Message},
                 403: {"model": general_schema.Message},
                 404: {"model": general_schema.Message},
                 500: {"model": general_schema.Message}
             },
             response_model=auth_schema.LoginResponse)
def login(
    payload: auth_schema.LoginRequest,
    session: Session = Depends(get_session)
):
    """Docstring."""

    user = user_crud.get_user_by_email(email=payload.email, session=session)
    if not user:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "msg": f"User not found."
            })

    if not pwd_context.verify(payload.password, user.password):
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content={
                "msg": f"Invalid credentials."
            })

    access_token_expires = timedelta(minutes=30)
    access_token = jwt_encode(
        user_id=user.user_id,
        salt=user.salt_jwt,
        expires_delta=access_token_expires)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "access_token": access_token,
            "refresh_token": "refresh_token"
        })
