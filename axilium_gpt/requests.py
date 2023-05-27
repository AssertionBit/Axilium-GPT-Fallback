from pydantic import BaseModel


class Completions(BaseModel):
    ...


class ChatCompletions(BaseModel):
    ...


__all__ = (
    "Completions",
    "ChatCompletions",
)

