from typing import List

from pydantic import BaseModel


class Completions(BaseModel):
    model: str
    prompt: str
    max_tokens: int
    temperature: float
    top_p: int
    n: int
    stream: bool = False
    logprobs: str | None = None
    stop: str = "\n"


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatCompletions(BaseModel):
    model: str
    messages: List[ChatMessage]


__all__ = (
    "Completions",
    "ChatCompletions",
)
