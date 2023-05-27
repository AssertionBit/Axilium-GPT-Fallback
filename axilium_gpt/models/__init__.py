__all__ = (
    "DATABASE",
    "User",
    "create_tables",
)


from .base import DATABASE, CURSOR
from .message import Message
from .user import User


def create_tables():
    with DATABASE:
        DATABASE.create_tables([User, Message])

