import pytest
import uuid
from datetime import datetime
from sqlmodel import create_engine, SQLModel, Session

from src.reservation.adapter.repository import ORMRepository
from src.reservation.domain.commands import CreateReservation, ModifyReservation, DeleteReservation
from src.reservation.service import handlers


@pytest.fixture(scope="session")
def repository() -> ORMRepository:
    engine = create_engine("mysql+pymysql://test:test@localhost:3306/test", echo=True)
    session = Session(engine)
    SQLModel.metadata.create_all(engine)
    try:
        yield ORMRepository(session)
    finally:
        SQLModel.metadata.drop_all(engine)


def test_create_reservation(repository):
    cmd = CreateReservation(start_at=datetime(2021, 11, 1, 0, 0, 0), end_at=datetime(2021, 11, 1, 1, 0, 0),
                            created_by=uuid.uuid4(), name="TEST_RESERVATION")
    result = handlers.create_reservation(cmd=cmd, repo=repository)
    assert isinstance(result, int) is True


def test_modify_reservation(repository):
    cmd = ModifyReservation(start_at=datetime(2021, 11, 1, 0, 0, 0), end_at=datetime(2021, 11, 1, 2, 0, 0),
                            created_by=uuid.uuid4(), name="TEST_RESERVATION_v2", reservation_id=1)
    result = handlers.modify_reservation(cmd=cmd, repo=repository)
    assert isinstance(result.id, int) is True


def test_modified_and_delete_reservation(repository):
    cmd = DeleteReservation(reservation_id=1, user_id=uuid.uuid4())
    handlers.delete_reservation(cmd=cmd, repo=repository)
