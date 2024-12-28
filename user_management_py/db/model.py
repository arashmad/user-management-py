"""Docstring."""

import uuid
from datetime import datetime, timezone

from sqlmodel import CheckConstraint, Column, Field, SQLModel, String


def generate_pipeline_id(user_id: str) -> str:
    """Generate unique pipeline id from user id."""
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, f"{user_id}-{str(get_datetime_utc_now())}"))


def get_datetime_utc_now() -> datetime:
    """Get current datetime in UTC."""
    utc_now = datetime.now(tz=timezone.utc)
    return utc_now


class Pipelines(SQLModel, table=True):
    """Docstring."""

    pipeline_id: str = Field(
        title="Pipeline ID",
        description="Unique identifier for the pipeline",
        primary_key=True)
    pipeline_name: str = Field(
        title="Pipeline Name",
        description="Name of the pipeline")
    pipeline_description: str | None = Field(
        title="Pipeline Description",
        description="A short description of the pipeline")
    pipeline_type: str = Field(
        title="Pipeline Type",
        description="Type of the pipeline from list ['sentinel', 'misac', 'xregnet']",
        sa_column=Column(String, nullable=False))
    status: str = Field(
        title="Status",
        description="Status of the pipeline from list ['running', 'completed', 'failed']",
        default='running',
        sa_column=Column(String, nullable=False))
    status_message: str | None = Field(
        title="Status Message",
        description="Status message of the pipeline")
    created_at: datetime = Field(
        title="Created At",
        description="Timestamp of when the pipeline was created.",
        default_factory=get_datetime_utc_now())
    started_at: datetime | None = Field(
        title="Started At",
        description="Timestamp of when the pipeline was started.")
    finished_at: datetime | None = Field(
        title="Finished At",
        description="Timestamp of when the pipeline was finished.")

    # FK for Users table
    user_id: str = Field(
        title="User ID",
        description="Unique identifier for the user.",
        foreign_key="users.user_id")

    # Constraints
    __table_args__ = (
        CheckConstraint(
            pipeline_type.sa_column in ['sentinel', 'misac', 'xregnet']),
        CheckConstraint(
            status.sa_column in ['running', 'completed', 'failed'])
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.pipeline_id:
            self.pipeline_id = generate_pipeline_id(self.user_id)
