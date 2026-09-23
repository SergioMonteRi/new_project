from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface
from src.schemas.create_person_schema import CreatePersonSchema

from .interfaces.person_creator_controller import PersonCreatorControllerInterface


class PersonCreatorController(PersonCreatorControllerInterface):
    def __init__(self, people_repository: PeopleRepositoryInterface):
        self.__people_repository = people_repository

    def create_person(self, person_data: CreatePersonSchema) -> dict:
        first_name = person_data.first_name
        last_name = person_data.last_name
        age = person_data.age
        pet_id = person_data.pet_id

        self.__insert_person_in_db(first_name, last_name, age, pet_id)

        return self.__format_response(person_data)

    def __insert_person_in_db(
        self, first_name: str, last_name: str, age: int, pet_id: int
    ) -> None:
        self.__people_repository.insert_person(first_name, last_name, age, pet_id)

    def __format_response(self, person_info: CreatePersonSchema) -> dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": person_info.model_dump(),
            }
        }
