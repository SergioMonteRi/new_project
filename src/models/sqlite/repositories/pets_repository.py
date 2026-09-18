from typing import List

from sqlalchemy import select

from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.settings.connection import DBConnectionHandler


class PetsRepository:
    def __init__(self, db_connection: DBConnectionHandler) -> None:
        self.__db_connection = db_connection

    def list_pets(self) -> List:
        with self.__db_connection as session:
            return session.scalars(select(PetsTable)).all()
