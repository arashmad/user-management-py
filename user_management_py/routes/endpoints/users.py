"""
Fastapi Poetry Boilerplate.

A boilerplate for fastapi python project supported by poetry.
"""

import user_management_py.schemas.general as general_schema
import user_management_py.schemas.users as users_schema
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlmodel import Session
from user_management_py.db.connection import get_session
from user_management_py.models.users import Users

router = APIRouter()


@router.post('/',
             summary="Create a new user",
             response_model=users_schema.CreateUserResponse,
             responses={
                 401: {"model": general_schema.Message},
                 404: {"model": general_schema.Message},
                 500: {"model": general_schema.Message}})
def create_user(
        user: users_schema.CreateUserRequest,
        session: Session = Depends(get_session)):
    """Docstring."""

    new_user = Users(email=user.email, password=user.password)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "user": new_user.to_dict()
        })
