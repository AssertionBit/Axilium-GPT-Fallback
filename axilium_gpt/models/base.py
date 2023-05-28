from os import environ

from peewee import *

DATABASE: SqliteDatabase = SqliteDatabase(
    "auxilium-gpt-fallback.db", pragmas={"journal_mode": "wal"}
)


__all__ = ("DATABASE",)
