"""
Fastapi Poetry Boilerplate.

A boilerplate for fastapi python project supported by poetry.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from user_management_py.core import setting as environment
from user_management_py.core.config_parser import config
from user_management_py.routes.api import router

APP_NAME = config['meta']['app_name']
APP_DESC = config['meta']['app_description']
APP_VERSION = config['meta']['app_version']
APP_TERMS = config['meta']['app_terms']
APP_DOC_NAME = config['meta']['app_doc_name']

CONTACT_NAME = config['maintainer']['name']
CONTACT_LINK = config['maintainer']['link']
CONTACT_MAIL = config['maintainer']['mail']


if environment.SERVICE_NAMESPACE:
    SERVICE_NAMESPACE = environment.SERVICE_NAMESPACE
    DOCS_URL = f'/{SERVICE_NAMESPACE}/docs'
    REDOCS_URL = f'/{SERVICE_NAMESPACE}/redoc'
    OPENAPI_URL = f'/{SERVICE_NAMESPACE}/{APP_DOC_NAME}.json'
else:
    DOCS_URL = '/docs'
    REDOCS_URL = '/redoc'
    OPENAPI_URL = f'/{APP_DOC_NAME}.json'


fastapi_app = FastAPI(
    title=APP_NAME,
    description=APP_DESC,
    version=APP_VERSION,
    terms_of_service=APP_TERMS,
    contact={
        "name": CONTACT_NAME,
        "url": CONTACT_LINK,
        "email": CONTACT_MAIL,
    },
    docs_url=DOCS_URL,
    redoc_url=REDOCS_URL,
    openapi_url=OPENAPI_URL,
    root_path=environment.ROOT_PATH)


fastapi_app.add_middleware(
    CORSMiddleware,
    allow_origins=environment.ALLOWED_CLIENT,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])


if environment.SERVICE_NAMESPACE:
    fastapi_app.include_router(router, prefix=f'/{SERVICE_NAMESPACE}')
else:
    fastapi_app.include_router(router)


app = fastapi_app
