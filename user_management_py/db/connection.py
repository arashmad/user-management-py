"""Docstring."""


from sqlmodel import Session, SQLModel, create_engine

from user_management_py.models.users import Users  # noqa # pylint: disable=unused-import
from user_management_py.models.pipelines import Pipelines  # noqa # pylint: disable=unused-import

DBNAME = "database.db"
DATABASE_URL = f"sqlite:///{DBNAME}"

engine = create_engine(DATABASE_URL)

SQLModel.metadata.create_all(engine)


def get_session():
    """Docstring."""
    with Session(engine) as session:
        yield session
