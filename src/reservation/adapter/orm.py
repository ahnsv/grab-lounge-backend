from datetime import datetime
from typing import Optional

from src.reservation.domain.models import Reservation
from sqlmodel import SQLModel, Field


class ReservationInDB(Reservation, SQLModel, table=True):
    __tablename__ = "reservations"
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
