from typing import Dict

from src.models.sqlite.dto.person_with_pet import PersonWithPet
from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface


class PersonFinderController:
    def __init__(self, people_repository: PeopleRepositoryInterface):
        self.__people_repository = people_repository

    def find_person_by_id(self, person_id: int) -> Dict:
        person = self.__find_person_in_db(person_id)

        return self.__format_response(person)

    def __find_person_in_db(self, person_id):
        person = self.__people_repository.get_person(person_id)

        if not person:
            raise Exception("Person not found")

        return person

    def __format_response(self, person: PersonWithPet) -> Dict:
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
