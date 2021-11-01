from datetime import datetime
from enum import Enum
from typing import Union
from uuid import uuid4, UUID

from pydantic import BaseModel, Field


class ReservationStatus(int, Enum):
    PENDING = 0
    APPROVED = 1
    REJECTED = 2


class Reservation(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str = Field(default=None)
    start_at: datetime
    end_at: datetime
    created_by: UUID
    status: int
