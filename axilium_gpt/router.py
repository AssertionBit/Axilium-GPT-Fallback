from logging import Logger, getLogger

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

# from .model import model
from .models import *


logger: Logger = getLogger("rich")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Preparing application")
    create_tables()

    logger.info("Starting application")

    yield

    logger.warning("Application is shutting down!")
    logger.warning("Disconnecting from database")
    DATABASE.close()
    logger.info("Application shut down succsessfully")


app = FastAPI(lifespan=lifespan)


@app.get("/")
def index() -> JSONResponse:
    return JSONResponse(
        jsonable_encoder(
            {"message": {"status": "working", "model-name": model.model.model_name}}
        )
    )


@app.get("/models")
def models() -> JSONResponse:
    global model

    return JSONResponse(model.list_models())


__all__ = ("app",)
