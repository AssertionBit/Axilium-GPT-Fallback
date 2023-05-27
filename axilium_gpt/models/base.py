from os import environ
from peewee import *


DATABASE: PostgresqlDatabase = PostgresqlDatabase(
    database=environ.get("PG_DATABASE"),
    user=environ.get("PG_USERNAME"),
    password=environ.get("PG_PASSWORD"),
    port=5432,
)

CURSOR: CursorWrapper = DATABASE.cursor()


__all__ = ("DATABASE",)
