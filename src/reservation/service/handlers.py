from datetime import datetime
from typing import List

from src.reservation.adapter.http_client import HTTPClient
from src.reservation.adapter.orm import ReservationInDB
from src.reservation.adapter.repository import ORMRepository
from src.reservation.container import Container
from src.reservation.domain import commands

from dependency_injector.wiring import inject, Provide
from fastapi.exceptions import HTTPException
from src.reservation.service import NoUserIDFoundError


@inject
def create_reservation(
    cmd: commands.CreateReservation,
    repo: ORMRepository = Provide[Container.repo],
    external_service_client: HTTPClient = Provide[Container.http_client],
):
    try:
        check_if_user_exists(cmd.created_by, external_service_client)
    except NoUserIDFoundError as exc:
        raise HTTPException(status_code=exc.code, detail=exc.message)
    new_reservation = ReservationInDB(status=0, **cmd.dict(exclude_unset=True))
    return repo.add(new_reservation)


def check_if_user_exists(user_id, external_service_client):
    user = external_service_client.request("GET", f"/{user_id}")
    if not user:
        raise NoUserIDFoundError(message="유저 아이디를 찾을 수 없습니다")


@inject
def modify_reservation(
    cmd: commands.ModifyReservation, repo: ORMRepository = Provide[Container.repo]
):
    [existing_reservation] = repo.get(cmd.reservation_id)  # type: ReservationInDB
    for key, value in cmd.dict(exclude_unset=True, exclude={"reservation_id"}).items():
        setattr(existing_reservation, key, value)
    existing_reservation.updated_at = datetime.now()
    repo.session.add(existing_reservation)
    repo.session.commit()
    return existing_reservation


@inject
def delete_reservation(
    cmd: commands.DeleteReservation, repo: ORMRepository = Provide[Container.repo]
):
    [existing_reservation] = repo.get(cmd.reservation_id)
    repo.session.delete(existing_reservation)
    repo.session.commit()
