from fastapi import APIRouter

from src.reservation.domain.commands import CreateReservation, ModifyReservation, DeleteReservation
from src.reservation.presentation.fastapi.schema import NewReservationIn, UpdateReservationIn
from src.reservation.service.messagebus import messagebus

router = APIRouter()


@router.post("/reservation")
def new_reservation(body: NewReservationIn):
    cmd = CreateReservation(**body.dict())
    messagebus.handle(cmd)


@router.patch("/reservation/{reservation_id}")
def update_reservation(reservation_id: int, body: UpdateReservationIn):
    cmd = ModifyReservation(reservation_id=reservation_id, **body.dict())
    messagebus.handle(cmd)


@router.delete("/reservation/{reservation_id}")
def delete_reservation(reservation_id: int):
    cmd = DeleteReservation(reservation_id=reservation_id)
    messagebus.handle(cmd)
