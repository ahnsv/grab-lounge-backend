from src.reservation.adapter.orm import ReservationInDB
from src.reservation.adapter.repository import ORMRepository
from src.reservation.container import Container
from src.reservation.domain import commands

from dependency_injector.wiring import inject, Provide


@inject
def create_reservation(cmd: commands.CreateReservation, repo: ORMRepository = Provide[Container.repo]):
    new_reservation = ReservationInDB(status=0, **cmd.dict(exclude_unset=True))
    return repo.add(new_reservation)


@inject
def modify_reservation(cmd: commands.ModifyReservation, repo: ORMRepository = Provide[Container.repo]):
    [existing_reservation] = repo.get(cmd.reservation_id)
    for key, value in cmd.dict(exclude_unset=True, exclude={"reservation_id"}).items():
        setattr(existing_reservation, key, value)
    repo.session.add(existing_reservation)
    repo.session.commit()
    return existing_reservation


@inject
def delete_reservation(cmd: commands.DeleteReservation, repo: ORMRepository = Provide[Container.repo]):
    [existing_reservation] = repo.get(cmd.reservation_id)
    repo.session.delete(existing_reservation)
    repo.session.commit()
