from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface

from .interfaces.pet_delete_controller import PetDeleteControllerInterface


class PetDeleteController(PetDeleteControllerInterface):
    def __init__(self, pet_repository: PetsRepositoryInterface):
        self.__pet_repository = pet_repository

    def delete_pet(self, pet_id: int) -> bool:
        return self.__pet_repository.delete_pet(pet_id)
