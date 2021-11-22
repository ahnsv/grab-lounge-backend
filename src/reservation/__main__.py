import uvicorn

from src.reservation.presentation.fastapi.app import create_app

if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app)
