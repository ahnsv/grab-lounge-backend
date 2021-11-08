import os
import sys

from fastapi import FastAPI

from src.reservation.container import Container
from src.reservation.presentation.fastapi.routers import router


def create_app():
    app = FastAPI()
    app.include_router(router)
    container = Container()
    container.config.from_dict({"db_url": os.getenv("DB_URL", "")})
    container.wire(packages=[sys.modules["src.reservation"]])
    container.database().create_all()

    return app
