from contextlib import asynccontextmanager
from logging import Logger, getLogger

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from .model import model
from .models import *
from .requests import *

logger: Logger = getLogger("rich")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Preparing application")
    create_tables()

    logger.info("Starting application")
    logger.info(f"Listening to 8000 port")
    logger.info(f"OpenAPI docs at {app.openapi_url}")

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


@app.post("/completions")
def completions(request: Completions) -> JSONResponse:
    global model, logger

    result = model.generate(completions.prompt, streaming=False)

    return JSONResponse(
        jsonable_encoder(
            {
                "id": "cmpl-uqkvlQyYK7bGYrRHQ0eXlWi7",
                "object": "text_completion",
                "created": 1589478378,
                "model": model.model.model_name,
                "choices": [
                    {
                        "text": result,
                        "index": 0,
                        "logprobs": None,
                        "finish_reason": "length",
                    }
                ],
                "usage": {
                    "prompt_tokens": request.prompt.__len__(),
                    "completion_tokens": result.__len__(),
                    "total_tokens": request.prompt.__len__() + result.__len__(),
                },
            }
        )
    )


@app.post("/chat/completions")
def chat_completions(req: ChatCompletions) -> JSONResponse:
    global model, logger

    def calc_prompt_len(req: ChatCompletions) -> int:
        length = 0

        for msg in req.messages:
            length += len(msg.role)
            length += len(msg.content)

        return length

    message = model.chat_completion(
        [msg.dict() for msg in req.messages], streaming=False
    )

    return JSONResponse(
        jsonable_encoder(
            {
                "id": "chatcmpl-123",
                "object": "chat.completion",
                "created": 1677652288,
                "choices": [
                    {
                        "index": 0,
                        "message": {"role": "assistant", "content": message},
                        "finish_reason": "stop",
                    }
                ],
                "usage": {
                    "prompt_tokens": calc_prompt_len(req),
                    "completion_tokens": len(message),
                    "total_tokens": 21,
                },
            }
        )
    )


__all__ = ("app",)
