"""
Fastapi Poetry Boilerplate.

A boilerplate for fastapi python project supported by poetry.
"""

import user_management_py.routes.endpoints.home as home_route
import user_management_py.routes.endpoints.pipelines as pipelines_route
import user_management_py.routes.endpoints.users as users_route
from fastapi import APIRouter

router = APIRouter()

router.include_router(home_route.router, tags=["Home"])
router.include_router(users_route.router, tags=["Users"],
                      prefix="/users")
# router.include_router(pipelines_route.router, tags=["Pipelines"],
#                       prefix="/pipelines")
