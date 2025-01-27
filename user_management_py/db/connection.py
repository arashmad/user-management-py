"""Docstring."""


from sqlmodel import Session, SQLModel, create_engine

from user_management_py.models.users import Users  # noqa # pylint: disable=unused-import
from user_management_py.models.pipelines import Pipelines  # noqa # pylint: disable=unused-import

DBNAME = "database.db"
DATABASE_URL = f"sqlite:///{DBNAME}"

engine = create_engine(DATABASE_URL)


def init_db():
    """
    Initialize the database by creating all tables.

    This function uses the SQLModel metadata to create all tables defined in the
    models if they do not already exist in the database.
    """
    SQLModel.metadata.create_all(engine)


def get_session():
    """
    Get a database session.

    This function yields a session object for interacting with the database
    using SQLModel.

    Yields
    ------
    session : Session
        A SQLModel session object connected to the database.
    """
    with Session(engine) as session:
        yield session
