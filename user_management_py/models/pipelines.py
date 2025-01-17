"""
Fastapi Poetry Boilerplate.

A boilerplate for fastapi python project supported by poetry.
"""


from datetime import datetime
from sqlmodel import CheckConstraint, Field, SQLModel

from user_management_py.utils.id import \
    get_datetime_utc_now, generate_pipeline_id


class BasePipeline(SQLModel):
    """Base Pipeline model."""

    pipeline_name: str = Field(
        title="Pipeline Name",
        description="Name of the pipeline"
    )
    pipeline_description: str | None = Field(
        title="Pipeline Description",
        description="A short description of the pipeline"
    )
    pipeline_type: str = Field(
        title="Pipeline Type",
        description="Type of the pipeline from list ['sentinel', 'misac', 'xregnet']"
    )


class PipelineCreate(BasePipeline):
    """
    Inherit from `BasePipeline` model.

    It is used to create a new pipeline.
    """


class PipelineRead(BasePipeline):
    """
    Inherit from `BasePipeline` model.

    It is used to read a user.
    """

    pipeline_id: str = Field(
        title="Pipeline ID",
        description="Unique identifier for the pipeline"
    )
    status: str = Field(
        title="Status",
        description="Status of the pipeline from list "
        "['not_started', 'running', 'completed', 'failed']"
    )
    status_message: str | None = Field(
        title="Status Message",
        description="Status message of the pipeline"
    )
    created_at: datetime = Field(
        title="Created At",
        description="Timestamp of when the pipeline was created."
    )
    started_at: datetime | None = Field(
        title="Started At",
        description="Timestamp of when the pipeline was started."
    )
    finished_at: datetime | None = Field(
        title="Finished At",
        description="Timestamp of when the pipeline was finished."
    )

    # FK for Users table
    user_id: str = Field(
        title="User ID",
        description="Unique identifier for the user "
        "who is the owner of the pipeline.",
    )


class Pipelines(BasePipeline, table=True):
    """
    Inherit from `BasePipeline` model.

    It is used to create a new pipeline in the database.
    """

    pipeline_id: str = Field(
        title="Pipeline ID",
        description="Unique identifier for the pipeline",
        primary_key=True
    )
    pipeline_type: str = Field(
        title="Pipeline Type",
        description="Type of the pipeline from list ['sentinel', 'misac', 'xregnet']",
    )
    status: str = Field(
        title="Status",
        description="Status of the pipeline from list "
        "['not_started', 'running', 'completed', 'failed']",
        default='not_started',
    )
    status_message: str | None = Field(
        title="Status Message",
        description="Status message of the pipeline",
        default="Pipeline has not started yet."
    )
    created_at: datetime = Field(
        title="Created At",
        description="Timestamp of when the pipeline was created.",
        default_factory=get_datetime_utc_now
    )
    started_at: datetime | None = Field(
        title="Started At",
        description="Timestamp of when the pipeline was started."
    )
    finished_at: datetime | None = Field(
        title="Finished At",
        description="Timestamp of when the pipeline was finished."
    )

    # FK for Users table
    user_id: str = Field(
        title="User ID",
        description="Unique identifier for the user.",
        foreign_key="users.user_id"
    )

    # Constraints
    __table_args__ = (
        CheckConstraint(
            pipeline_type.sa_column in ['sentinel', 'misac', 'xregnet']),
        CheckConstraint(
            status.sa_column in ['running', 'completed', 'failed'])
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.pipeline_id and self.user_id:
            self.pipeline_id = generate_pipeline_id(self.user_id)

    def to_dict(self, exclude_none: bool = False) -> dict:
        """
        Convert the model instance to a dictionary.

        :param exclude_none: Exclude fields with None values if True.
        :return: Dictionary representation of the instance.
        """
        model_dict = self.model_dump(exclude_none=exclude_none)

        for key, value in model_dict.items():
            print(key, value)
            if isinstance(value, datetime):
                model_dict[key] = value.isoformat()

        return model_dict
