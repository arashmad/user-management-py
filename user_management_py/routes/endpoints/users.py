"""
Fastapi Poetry Boilerplate.

A boilerplate for fastapi python project supported by poetry.
"""

from sqlmodel import Session


from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from user_management_py.db.connection import get_session
from user_management_py.models.users import Users
from user_management_py.utils.auth import pwd_context

import user_management_py.schemas.general as general_schema
import user_management_py.schemas.users as users_schema


router = APIRouter(tags=["Users"], prefix="/users")


@router.post('/',
             summary="Create a new user",
             response_model=users_schema.CreateUserResponse,
             responses={
                 401: {"model": general_schema.Message},
                 404: {"model": general_schema.Message},
                 500: {"model": general_schema.Message}})
def create_user(
        payload: users_schema.CreateUserRequest,
        session: Session = Depends(get_session)):
    """Docstring."""
    password_hash = pwd_context.hash(payload.password)
    new_user = Users(email=payload.email, password=password_hash)

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "user": new_user.to_dict()
        })
