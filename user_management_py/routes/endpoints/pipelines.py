"""
Fastapi Poetry Boilerplate.

A boilerplate for fastapi python project supported by poetry.
"""

from sqlmodel import Session, select

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from user_management_py.models.pipelines import Pipelines
from user_management_py.db.connection import get_session
import user_management_py.crud.pipelines as crud_pipelines
from user_management_py.utils.jwt_bearer import JWTBearer

import user_management_py.schemas.general as general_schema
import user_management_py.schemas.pipelines as pipelines_schema

router = APIRouter(tags=["Pipelines"], prefix="/pipelines")


@router.get('/',
            dependencies=[Depends(JWTBearer())],
            summary="Fetch all pipelines",
            response_model=pipelines_schema.GetPipelinesRespons,
            responses={
                401: {"model": general_schema.Message},
                404: {"model": general_schema.Message},
                500: {"model": general_schema.Message}})
def get_all_pipelines(
        pipeline_type: str,
        session: Session = Depends(get_session),
        user_id: str = Depends(JWTBearer())):
    """Fetch all pipelines."""
    pipelines = crud_pipelines.fetch_pipeline_by_type(
        pipeline_type=pipeline_type,
        user_id=user_id,
        session=session)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "pipelines": pipelines
        })


@router.get('/{pipeline_id}',
            summary="Get pipeline with id",
            response_model=pipelines_schema.GetPipelineByIdResponse,
            responses={
                401: {"model": general_schema.Message},
                404: {"model": general_schema.Message},
                500: {"model": general_schema.Message}})
def get_pipeline(
        pipeline_id: str,
        session: Session = Depends(get_session),
        user_id: str = Depends(JWTBearer())):
    """Fetch a pipeline by ID."""
    pipeline = crud_pipelines.fetch_pipeline_by_id(
        pipeline_id=pipeline_id,
        user_id=user_id,
        session=session)

    if not pipeline:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "msg": f"Pipeline ({pipeline_id}) not found."
            })

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "pipeline": pipeline
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
        session: Session = Depends(get_session),
        user_id: str = Depends(JWTBearer())):
    """Create a new pipeline."""

    new_pipeline = crud_pipelines.create_pipeline(
        pipeline_name=pipeline.pipeline_name,
        pipeline_description=pipeline.pipeline_description,
        pipeline_type=pipeline.pipeline_type,
        user_id=user_id,
        session=session)

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "pipeline": new_pipeline.to_dict()
        })


@router.delete('/{pipeline_id}',
               summary="Delete pipeline with id",
               response_model=pipelines_schema.DeletePipelineResponse,
               responses={
                   401: {"model": general_schema.Message},
                   404: {"model": general_schema.Message},
                   500: {"model": general_schema.Message}})
def delete_pipeline(
        pipeline_id: str,
        session: Session = Depends(get_session),
        user_id: str = Depends(JWTBearer())):
    """Delete pipeline by id."""

    pipeline = crud_pipelines.delete_pipeline(
        pipeline_id=pipeline_id,
        user_id=user_id,
        session=session)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "pipeline": pipeline
        })
