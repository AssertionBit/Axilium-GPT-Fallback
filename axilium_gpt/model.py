from logging import getLogger as _getLogger
from os import mkdir as _mkdir

from gpt4all import GPT4All as _GPT4All


logger = _getLogger("rich")

logger.info("Loading model")

try:
    _mkdir("models")

except:
    ...

model: _GPT4All = _GPT4All('ggml-gpt4all-j.bin', model_path='models', allow_download=True)

__all__ = ("model",)

