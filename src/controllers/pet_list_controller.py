# pylint: disable=redefined-outer-name

from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface


class PetListController:
    def __init__(self, pet_repository: PetsRepositoryInterface):
        self.__pet_repository = pet_repository

    def list_pets(self) -> dict:
        pets = self.__get_pets_in_db()

        return self.__format_response(pets)

    def __get_pets_in_db(self) -> list[PetsTable]:
        pets = self.__pet_repository.list_pets()
        return pets

    def __format_response(self, pets: list[PetsTable]) -> dict:
        pets_list = [{"id": pet.id, "name": pet.name, "type": pet.type} for pet in pets]

        return {
            "data": {"type": "Pet", "count": len(pets_list), "attributes": pets_list}
        }
