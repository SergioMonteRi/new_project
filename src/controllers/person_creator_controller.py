import re
from typing import Dict

from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface


class PersonCreatorController:
    def __init__(self, people_repository: PeopleRepositoryInterface):
        self.__people_repository = people_repository

    def create_person(self, person_data: Dict) -> Dict:
        first_name = person_data["first_name"]
        last_name = person_data["last_name"]
        age = person_data["age"]
        pet_id = person_data["pet_id"]

        self.__validate_name(first_name)
        self.__validate_name(last_name)

        self.__insert_person_in_db(first_name, last_name, age, pet_id)

        return self.__format_response(person_data)

    def __validate_name(self, name: str) -> None:
        non_valid_characters = re.compile(r"[^a-zA-Z]")

        if non_valid_characters.search(name):
            raise Exception

    def __insert_person_in_db(
        self, first_name: str, last_name: str, age: int, pet_id: int
    ) -> None:
        self.__people_repository.insert_person(first_name, last_name, age, pet_id)

    def __format_response(self, person_info: Dict) -> Dict:
        return {"data": {"type": "Person", "count": 1, "attributes": person_info}}
