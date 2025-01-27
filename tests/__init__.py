"""
Initialization module for the tests package.

This module is responsible for setting up the testing environment and making
test-related functionality available to other parts of the project.
"""

import os

from fastapi import FastAPI

from sqlmodel import SQLModel, Session, create_engine
from sqlmodel.pool import StaticPool

from user_management_py.create_app import app
from user_management_py.db.connection import get_session


os.environ['service_namespace'] = 'test-service'

os.environ['ROOT_PATH'] = ''
os.environ['APP_PORT'] = "8000"
os.environ['ALLOWED_CLIENT'] = "*"

in_mem_engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)


def get_test_session():
    """
    Get a test database session.

    This function provides a session for interacting with the test database
    using an in-memory SQLite engine.

    Yields
    ------
    session : Session
        A SQLModel session connected to the in-memory SQLite database.
    """
    with Session(in_mem_engine) as session:
        yield session


def add_test_database():
    """
    Set up the test database.

    This function adds an in-memory SQLite database to the application by
    overriding the `get_session` dependency with a new session connected to the
    in-memory database. It then creates all tables in the database using the
    `SQLModel.metadata.create_all` method.

    """
    app.dependency_overrides[get_session] = get_test_session
    SQLModel.metadata.create_all(in_mem_engine)


def remove_test_database():
    """
    Tear down the test database.

    This function drops all tables in the database using the
    `SQLModel.metadata.drop_all` method and then creates all tables again
    using the `SQLModel.metadata.create_all` method. This ensures that the
    test database is deleted and recreated after each test.

    """
    SQLModel.metadata.drop_all(in_mem_engine)
    SQLModel.metadata.create_all(in_mem_engine)
