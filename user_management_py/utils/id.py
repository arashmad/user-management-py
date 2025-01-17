"""
Fastapi Poetry Boilerplate.

A boilerplate for fastapi python project supported by poetry.
"""


import os
import uuid
import binascii
from datetime import datetime, timezone


def get_datetime_utc_now() -> datetime:
    """Get current datetime in UTC."""
    utc_now = datetime.now(tz=timezone.utc)
    return utc_now


def generate_user_id(email: str) -> str:
    """Generate unique user id from email."""
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, email))


def generate_salt() -> str:
    """Generate random salt."""
    return binascii.hexlify(os.urandom(24)).decode('utf-8')


def generate_pipeline_id(user_id: str) -> str:
    """Generate unique pipeline id from user id."""
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, f"{user_id}-{str(get_datetime_utc_now())}"))
