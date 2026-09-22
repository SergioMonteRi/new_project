# pylint: disable=redefined-outer-name

from unittest.mock import Mock

import pytest

from src.controllers.person_finder_controller import PersonFinderController
from src.models.sqlite.dto.person_with_pet import PersonWithPet


@pytest.fixture
def people_repository():
    return Mock()


class TestPersonFinderController:
    def test_find_person_by_id(self, people_repository):
        people_repository.get_person.return_value = PersonWithPet(
            1, "John", "Doe", 30, "Max", "dog"
        )

        controller = PersonFinderController(people_repository)

        response = controller.find_person_by_id(1)

        people_repository.get_person.assert_called_once_with(1)

        assert response["data"]["type"] == "Person"
        assert response["data"]["attributes"]["id"] == 1

    def test_find_person_by_not_found_id(self, people_repository):
        people_repository.get_person.return_value = None

        controller = PersonFinderController(people_repository)

        with pytest.raises(Exception, match="Person not found"):
            controller.find_person_by_id(2)
