"""
Fastapi Poetry Boilerplate.

A boilerplate for fastapi python project supported by poetry.
"""

from pydantic import BaseModel, Field

from user_management_py.models.pipelines import PipelineCreate, PipelineRead


class GetPipelinesRespons(BaseModel):
    """Docstring."""

    pipelines: list[PipelineRead] = Field(
        title="Pipelines",
        description="List of pipelines.")

    model_config = {
        "json_schema_extra": {
            "title": "Message",
            "example": {
                "pipelines": [
                    {
                        "id": 1,
                        "pipeline_id": 1,
                        "pipeline_name": 1,
                        "pipeline_description": 1,
                        "pipeline_type": 1,
                        "status": 1,
                        "status_message": 1,
                        "created_at": 1,
                        "started_at": 1,
                        "finished_at": 1
                    }
                ]
            }
        }
    }


class GetPipelineByIdResponse(BaseModel):
    """Docstring."""

    pipeline: PipelineRead = Field(
        title="Pipeline",
        description="Pipeline details.")

    model_config = {
        "json_schema_extra": {
            "title": "Message",
            "example": {
                "pipeline":
                    {
                        "id": 1,
                        "pipeline_id": 1,
                        "pipeline_name": 1,
                        "pipeline_description": 1,
                        "pipeline_type": 1,
                        "status": 1,
                        "status_message": 1,
                        "created_at": 1,
                        "started_at": 1,
                        "finished_at": 1
                    }
            }
        }
    }


class CreatePipelineRequest(PipelineCreate):
    """Docstring."""

    model_config = {
        "json_schema_extra": {
            "title": "Message",
            "example": {
                "pipeline_name": "pick a name",
                "pipeline_description": "pick a description",
                "pipeline_type": "pick a type"
            }
        }
    }


class CreatePipelineResponse(BaseModel):
    """Docstring."""

    pipeline: PipelineRead = Field(
        title="Pipeline",
        description="Created pipeline.")

    model_config = {
        "json_schema_extra": {
            "title": "Message",
            "example": {
                "pipeline":
                    {
                        "id": 1,
                        "pipeline_id": 1,
                        "pipeline_name": 1,
                        "pipeline_description": 1,
                        "pipeline_type": 1,
                        "status": 1,
                        "status_message": 1,
                        "created_at": 1,
                        "started_at": 1,
                        "finished_at": 1
                    }
            }
        }
    }


class DeletePipelineResponse(BaseModel):
    """Docstring."""

    pipeline: PipelineRead = Field(
        title="Pipeline",
        description="Deleted pipeline.")

    model_config = {
        "json_schema_extra": {
            "title": "Message",
            "example": {
                "pipeline":
                    {
                        "id": 1,
                        "pipeline_id": 1,
                        "pipeline_name": 1,
                        "pipeline_description": 1,
                        "pipeline_type": 1,
                        "status": 1,
                        "status_message": 1,
                        "created_at": 1,
                        "started_at": 1,
                        "finished_at": 1
                    }
            }
        }
    }
