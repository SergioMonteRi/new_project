# pylint: disable=redefined-outer-name

from unittest.mock import Mock

import pytest

from src.schemas.create_person_schema import CreatePersonSchema

from .person_creator_controller import PersonCreatorController


@pytest.fixture
def people_repository():
    people_repository_mock = Mock()
    people_repository_mock.insert_person.return_value = None

    return people_repository_mock


@pytest.fixture
def person_data():
    person_data = {
        "first_name": "Developer",
        "last_name": "Tester",
        "age": 30,
        "pet_id": 10,
    }

    person = CreatePersonSchema.model_validate(person_data)

    return person


@pytest.fixture
def invalid_person_data():
    person_data = {
        "first_name": "Developer123",
        "last_name": "Tester123",
        "age": 30,
        "pet_id": 10,
    }

    person = CreatePersonSchema.model_validate(person_data)

    return person


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
