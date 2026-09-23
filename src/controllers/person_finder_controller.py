from src.exceptions.exception_types.http_bad_request import HttpBadRequestError
from src.exceptions.exception_types.http_not_found import HttpNotFoundError
from src.models.sqlite.dto.person_with_pet import PersonWithPet
from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface

from .interfaces.person_finder_controller import PersonFinderControllerInterface


class PersonFinderController(PersonFinderControllerInterface):
    def __init__(self, people_repository: PeopleRepositoryInterface):
        self.__people_repository = people_repository

    def find_person_by_id(self, person_id: int) -> dict:
        if person_id <= 0:
            raise HttpBadRequestError(message="Person id must be greater than zero")

        person = self.__find_person_in_db(person_id)

        return self.__format_response(person)

    def __find_person_in_db(self, person_id):
        person = self.__people_repository.get_person(person_id)

        if not person:
            raise HttpNotFoundError("Person not found")

        return person

    def __format_response(self, person: PersonWithPet) -> dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": {
                    "id": person.id,
                    "first_name": person.first_name,
                    "last_name": person.last_name,
                    "pet_name": person.pet_name,
                    "pet_type": person.pet_type,
                },
            }
        }
