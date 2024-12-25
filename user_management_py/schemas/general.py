"""
Fastapi Poetry Boilerplate.

A boilerplate for fastapi python project supported by poetry.
"""

from pydantic import BaseModel, Field


class Message(BaseModel):
    """A general template for those responses contain a message."""

    msg: str = Field(title="Message", description="Message from the API")

    model_config = {
        "json_schema_extra": {
            "title": "Message",
            "example": {
                "msg": "This is a test message coming from the API.",
            }
        }
    }
