from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4, uuid5, uuid3

from pybus.core.message import Command
from pydantic import Field


class BaseCommand(Command):
    id: UUID = Field(default_factory=uuid4)


class CreateReservation(BaseCommand):
    start_at: datetime
    end_at: datetime
    created_by: UUID
    name: str
    description: Optional[str]


class ModifyReservation(CreateReservation):
    reservation_id: int


class DeleteReservation(BaseCommand):
    reservation_id: int
    user_id: UUID
