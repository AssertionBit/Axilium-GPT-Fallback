from peewee import *

from .base import DATABASE


class Message(Model):
    class Meta:
        database = DATABASE


__all__ = ("Message",)
