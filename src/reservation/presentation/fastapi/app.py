from fastapi import FastAPI

from src.reservation.presentation.fastapi.routers import router


def create_app():
    app = FastAPI()
    app.include_router(router)

    return app
