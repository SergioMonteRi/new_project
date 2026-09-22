# pylint: disable=redefined-outer-name

from unittest.mock import Mock

import pytest

from .person_creator_controller import PersonCreatorController


@pytest.fixture
def people_repository():
    people_repository_mock = Mock()
    people_repository_mock.insert_person.return_value = None

    return people_repository_mock


@pytest.fixture
def person_data():
    return {
        "first_name": "Developer",
        "last_name": "Tester",
        "age": 30,
        "pet_id": 10,
    }


class TestPersonCreatorController:
    def test_create_person(self, people_repository, person_data):
        controller = PersonCreatorController(people_repository)
        response = controller.create_person(person_data)

        people_repository.insert_person.assert_called_once_with(
            "Developer",
            "Tester",
            30,
            10,
        )

        assert response["data"]["type"] == "Person"
        assert response["data"]["count"] == 1
        assert response["data"]["attributes"] == person_data

    def test_create_person_with_invalid_first_name(
        self, people_repository, person_data
    ):
        person_data["first_name"] = "Dev123"

        controller = PersonCreatorController(people_repository)

        with pytest.raises(Exception):
            controller.create_person(person_data)

    def test_create_person_with_invalid_last_name(self, people_repository, person_data):
        person_data["last_name"] = "Tester123"

        controller = PersonCreatorController(people_repository)

        with pytest.raises(Exception):
            controller.create_person(person_data)
