from src.reservation.adapter.orm import ReservationInDB
from src.reservation.adapter.repository import ORMRepository
from src.reservation.domain import commands


def create_reservation(cmd: commands.CreateReservation, repo: ORMRepository):
    new_reservation = ReservationInDB(status=0, **cmd.dict(exclude_unset=True))
    return repo.add(new_reservation)


def modify_reservation(cmd: commands.ModifyReservation, repo: ORMRepository):
    [existing_reservation] = repo.get(cmd.reservation_id)
    for key, value in cmd.dict(exclude_unset=True, exclude={"reservation_id"}).items():
        setattr(existing_reservation, key, value)
    repo.session.add(existing_reservation)
    repo.session.commit()
    return existing_reservation


def delete_reservation(cmd: commands.DeleteReservation, repo: ORMRepository):
    [existing_reservation] = repo.get(cmd.reservation_id)
    repo.session.delete(existing_reservation)
    repo.session.commit()
