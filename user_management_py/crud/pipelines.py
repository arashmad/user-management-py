"""Docstring."""

from sqlmodel import Session, select

from fastapi import HTTPException, status

from user_management_py.enum.pipeline import PipelineType
from user_management_py.models.pipelines import Pipelines, PipelineRead

PIPELINE_TYPES = [p.value for p in PipelineType]


def fetch_pipeline_by_type(
        pipeline_type: str, user_id: str, session: Session) -> list[PipelineRead]:
    """
    Fetch pipelines by type.

    Parameters
    ----------
    pipeline_type : str
        Type of the pipeline from list ['sentinel', 'misac', 'xregnet']
    user_id : str
        Unique identifier for the user.
    session : Session
        SQLModel Session object.

    Returns
    -------
    list[PipelineRead]
        List of pipelines.
    """
    try:
        if pipeline_type not in PIPELINE_TYPES:
            raise ValueError(
                f"Type ({pipeline_type}) not supported. Choose from [{PIPELINE_TYPES}].")

        query = \
            select(Pipelines).\
            where(Pipelines.pipeline_type == pipeline_type).\
            where(Pipelines.user_id == user_id)

        results = session.exec(query)
        return [pipeline.to_dict() for pipeline in results]

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)) from e


def fetch_pipeline_by_id(
        pipeline_id: str, user_id: str, session: Session) -> PipelineRead:
    """Fetch a pipeline by ID.

    Parameters
    ----------
    pipeline_id : str
        Unique identifier for the pipeline.
    user_id : str
        Unique identifier for the user.
    session : Session
        SQLModel Session object.

    Returns
    -------
    PipelineRead
        Pipeline details.
    """
    statement = \
        select(Pipelines).\
        where(Pipelines.pipeline_id == pipeline_id).\
        where(Pipelines.user_id == user_id)
    pipeline = session.exec(statement).first()

    if not pipeline:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pipeline ({pipeline_id}) not found.")

    return pipeline.to_dict()


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
