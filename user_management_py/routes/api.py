"""
Fastapi Poetry Boilerplate.

A boilerplate for fastapi python project supported by poetry.
"""

from fastapi import APIRouter

from user_management_py.routes.endpoints import home

router = APIRouter()

router.include_router(home.router, tags=["Home"])
