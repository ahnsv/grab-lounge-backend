import os

import databases
import sqlalchemy
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

from src.user.models import UserDB

DATABASE_URL = os.getenv("DB_URL", "sqlite:///./test.db")
database = databases.Database(DATABASE_URL)
Base: DeclarativeMeta = declarative_base()


class UserTable(Base, SQLAlchemyBaseUserTable):
    pass


engine = sqlalchemy.create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

users = UserTable.__table__


def get_user_db():
    yield SQLAlchemyUserDatabase(UserDB, database, users)
