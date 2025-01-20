"""
Fastapi Poetry Boilerplate.

A boilerplate for fastapi python project supported by poetry.
"""

from sqlmodel import Session, select

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from user_management_py.models.pipelines import Pipelines
from user_management_py.db.connection import get_session
from user_management_py.utils.jwt_bearer import JWTBearer

import user_management_py.schemas.general as general_schema
import user_management_py.schemas.pipelines as pipelines_schema

router = APIRouter(tags=["Pipelines"], prefix="/pipelines")


@router.get('/',
            dependencies=[Depends(JWTBearer())],
            summary="Get all pipelines",
            # response_model=pipelines_schema.GetPipelinesRespons,
            responses={
                401: {"model": general_schema.Message},
                404: {"model": general_schema.Message},
                500: {"model": general_schema.Message}})
def get_all_pipelines(
        skip: int = 0, limit: int = 100, session: Session = Depends(get_session), user_info: dict = Depends(JWTBearer())):
    """Docstring."""
    # pipelines = session.exec(select(Pipelines).offset(skip).limit(limit)).all()

    return user_info

    # return JSONResponse(
    #     status_code=status.HTTP_200_OK,
    #     content={
    #         "pipelines": pipelines
    #     })


@router.get('/{pipeline_id}',
            summary="Get pipeline with id",
            response_model=pipelines_schema.GetPipelineByIdResponse,
            responses={
                401: {"model": general_schema.Message},
                404: {"model": general_schema.Message},
                500: {"model": general_schema.Message}})
def get_pipeline(pipeline_id: str, session: Session = Depends(get_session)):
    """Docstring."""
    statement = select(Pipelines).where(Pipelines.pipeline_id == pipeline_id)
    pipeline = session.exec(statement).first()

    if not pipeline:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "msg": f"Pipeline ({pipeline_id}) not found."
            })

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "pipeline": {}
        })


@router.post('/',
             summary="Create a new pipeline",
             response_model=pipelines_schema.CreatePipelineResponse,
             responses={
                 401: {"model": general_schema.Message},
                 404: {"model": general_schema.Message},
                 500: {"model": general_schema.Message}})
def create_pipeline(
        pipeline: pipelines_schema.CreatePipelineRequest,
        session: Session = Depends(get_session)):
    """Docstring."""
    new_pipeline = Pipelines(
        pipeline_name=pipeline.pipeline_name,
        pipeline_description=pipeline.pipeline_description,
        pipeline_type=pipeline.pipeline_type)

    session.add(new_pipeline)
    session.commit()
    session.refresh(new_pipeline)

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "pipeline": new_pipeline
        })


@router.delete('/{pipeline_id}',
               summary="Delete pipeline with id",
               response_model=pipelines_schema.DeletePipelineResponse,
               responses={
                   401: {"model": general_schema.Message},
                   404: {"model": general_schema.Message},
                   500: {"model": general_schema.Message}})
def delete_pipeline(pipeline_id: str, session: Session = Depends(get_session)):
    """Docstring."""

    pipeline_in_db = session.get(Pipelines, pipeline_id)

    if not pipeline_in_db:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "msg": f"Pipeline ({pipeline_in_db.pipeline_id}) not found."
            })

    session.delete(pipeline_in_db)
    session.commit()

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "pipeline": pipeline_in_db
        })
