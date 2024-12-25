"""
Fastapi Poetry Boilerplate.

A boilerplate for fastapi python project supported by poetry.
"""


import os

import user_management_py

SERVICE_NAMESPACE = ""

ROOT_PATH = os.environ['ROOT_PATH'] if "ROOT_PATH" in os.environ else ""

ROOT_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(user_management_py.__file__),
        ".."))


APP_PORT = os.environ['APP_PORT']
ALLOWED_CLIENT = os.environ['ALLOWED_CLIENT'] if "ALLOWED_CLIENT" in os.environ else "*"
