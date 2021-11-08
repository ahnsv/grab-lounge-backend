from dependency_injector import containers, providers
from sqlmodel import create_engine, Session, SQLModel

from src.reservation.adapter.repository import ORMRepository


class Database:
    def __init__(self, engine) -> None:
        self.engine = engine

    def create_all(self):
        SQLModel.metadata.create_all(self.engine)

    def drop_all(self):
        SQLModel.metadata.drop_all(self.engine)


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    engine = providers.Singleton(create_engine, config.db_url)
    session = providers.Singleton(Session, engine)
    database = providers.Singleton(Database, engine)
    repo = providers.Factory(ORMRepository, session)

