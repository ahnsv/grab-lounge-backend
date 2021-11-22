from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from src.reservation.domain.models import ReservationStatus


class BaseSchema(BaseModel):
    pass


class NewReservationIn(BaseSchema):
    start_at: datetime
    end_at: datetime
    created_by: UUID
    name: str
    description: Optional[str]


class UpdateReservationIn(NewReservationIn):
    status: ReservationStatus
