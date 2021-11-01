from sqlmodel import Session, select, insert

from src.reservation.adapter.orm import ReservationInDB


class ReservationNotFound(Exception):
    pass


class ORMRepository:
    def __init__(self, session: Session):
        self.session = session

    def get(self, ref: int):
        stmt = select(ReservationInDB).where(ReservationInDB.id == ref).limit(1)
        result = self.session.execute(stmt).first()
        if not result:
            raise ReservationNotFound()
        return result

    def add(self, entity: ReservationInDB):
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        return entity.id
