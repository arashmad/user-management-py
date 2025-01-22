"""Docstring."""

from sqlmodel import Session

from fastapi import HTTPException, status

from user_management_py.models.pipelines import Pipelines, PipelineRead


def create_pipeline(
        pipeline_name: str,
        pipeline_description: str,
        pipeline_type: str,
        user_id: str,
        session: Session) -> PipelineRead:
    """Create a new pipeline."""
    try:
        new_pipeline = Pipelines(
            pipeline_name=pipeline_name,
            pipeline_description=pipeline_description,
            pipeline_type=pipeline_type,
            user_id=user_id)
        session.add(new_pipeline)
        session.commit()
        session.refresh(new_pipeline)
        return new_pipeline

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)) from e
