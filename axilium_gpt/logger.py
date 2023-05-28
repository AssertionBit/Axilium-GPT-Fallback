from logging import basicConfig

from rich.logging import RichHandler

basicConfig(
    level="NOTSET",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)],
)

__all__ = ()
