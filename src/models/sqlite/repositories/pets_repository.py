from typing import List

from sqlalchemy import select

from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface
from src.models.sqlite.settings.connection import DBConnectionHandler


class PetsRepository(PetsRepositoryInterface):
    def __init__(self, db_connection: DBConnectionHandler) -> None:
        self.__db_connection = db_connection

    def list_pets(self) -> List[PetsTable]:
        with self.__db_connection as session:
            return session.scalars(select(PetsTable)).all()

    def delete_pet(self, pet_id: int) -> bool:
        with self.__db_connection as session:
            stmt = select(PetsTable).where(PetsTable.id == pet_id)

            current_pet = session.scalar(stmt)

            if current_pet is None:
                return False

            session.delete(current_pet)
            session.commit()

            return True
