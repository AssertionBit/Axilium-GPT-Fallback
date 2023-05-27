from logging import getLogger as _getLogger
from os import mkdir as _mkdir

from gpt4all import GPT4All as _GPT4All


logger = _getLogger("rich")

logger.info("Loading model")
model: _GPT4All = None

try:
    _mkdir("models")

except:
    ...

try:
    # NOTE: For my hardware this isn't working at all
    # model: _GPT4All = _GPT4All('ggml-gpt4all-l13b-snoozy.bin', model_path='models', allow_download=True)
    pass

except Exception as e:
    logger.error(e, stack_info=True)


__all__ = ("model",)
