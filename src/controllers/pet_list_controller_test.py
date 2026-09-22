from unittest.mock import Mock

import pytest

from src.controllers.pet_list_controller import PetListController
from src.models.sqlite.entities.pets import PetsTable


@pytest.fixture
def pet_repository():
    pet_repository_mock = Mock()

    pet_repository_mock.list_pets.return_value = [
        PetsTable(id=1, name="Toto", type="dog"),
        PetsTable(id=2, name="Orange", type="cat"),
    ]

    return pet_repository_mock


class TestPersonFinderController:
    def test_list_pets(self, pet_repository):
        controller = PetListController(pet_repository)

        response = controller.list_pets()

        pet_repository.list_pets.assert_called_once()

        assert response["data"]["type"] == "Pets"
        assert response["data"]["count"] == 2
        assert response["data"]["attributes"][0]["name"] == "Toto"
