from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from src.models.sqlite.dto.person_with_pet import PersonWithPet
from src.models.sqlite.entities.people import PeopleTable
from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface
from src.models.sqlite.settings.connection import DBConnectionHandler


class PeopleRepository(PeopleRepositoryInterface):
    def __init__(self, db_connection: DBConnectionHandler) -> None:
        self.__db_connection = db_connection

    def insert_person(
        self, first_name: str, last_name: str, age: int, pet_id: int
    ) -> None:
        with self.__db_connection as session:
            try:
                person_data = PeopleTable(
                    first_name=first_name, last_name=last_name, age=age, pet_id=pet_id
                )

                session.add(person_data)
                session.commit()

            except SQLAlchemyError:
                session.rollback()
                raise

    def get_person(self, person_id: int) -> PersonWithPet | None:
        with self.__db_connection as session:
            stmt = (
                select(
                    PeopleTable.id,
                    PeopleTable.first_name,
                    PeopleTable.last_name,
                    PeopleTable.age,
                    PetsTable.name.label("pet_name"),
                    PetsTable.type.label("pet_type"),
                )
                .outerjoin(PetsTable, PetsTable.id == PeopleTable.pet_id)
                .where(PeopleTable.id == person_id)
            )

            person = session.execute(stmt).one_or_none()

            return person
