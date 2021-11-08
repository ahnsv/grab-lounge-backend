from uuid import UUID

from fastapi import APIRouter

from src.reservation.domain.commands import CreateReservation, ModifyReservation, DeleteReservation
from src.reservation.presentation.fastapi.schema import NewReservationIn, UpdateReservationIn
from src.reservation.service.messagebus import messagebus

router = APIRouter()


@router.post("/reservation")
def new_reservation(body: NewReservationIn):
    cmd = CreateReservation(**body.dict())
    [reservation_id] = messagebus.handle(cmd)
    return {"reservation_id": reservation_id}


@router.patch("/reservation/{reservation_id}")
def update_reservation(reservation_id: int, body: UpdateReservationIn):
    cmd = ModifyReservation(reservation_id=reservation_id, **body.dict())
    [updated_reservation] = messagebus.handle(cmd)
    return updated_reservation


@router.delete("/reservation/{reservation_id}")
def delete_reservation(reservation_id: int, user_id: UUID):
    cmd = DeleteReservation(reservation_id=reservation_id, user_id=user_id)
    messagebus.handle(cmd)
