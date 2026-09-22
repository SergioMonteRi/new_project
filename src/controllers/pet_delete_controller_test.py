from unittest.mock import Mock

from .pet_delete_controller import PetDeleteController


class TestPetDeleteController:
    def test_delete_pet(self):
        pet_repository = Mock()

        pet_repository.delete_pet.return_value = None

        controller = PetDeleteController(pet_repository)

        controller.delete_pet(1)

        pet_repository.delete_pet.assert_called_once_with(1)
