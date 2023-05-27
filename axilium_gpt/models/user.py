from peewee import *

from .base import DATABASE


class User(Model):
    id: IntegerField = IntegerField(
        null=False, column_name="id", index=True, unique=True, primary_key=True
    )

    class Meta:
        database = DATABASE


__all__ = ("User",)
