"""
Fastapi Poetry Boilerplate.

A boilerplate for fastapi python project supported by poetry.
"""

from fastapi import APIRouter

import user_management_py.routes.endpoints.home as home_route
import user_management_py.routes.endpoints.users as users_route

router = APIRouter()

router.include_router(home_route.router, tags=["Home"])
router.include_router(users_route.router, tags=["Users"],
                      prefix="/users")
