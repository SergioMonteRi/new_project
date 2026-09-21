from unittest.mock import Mock

from src.models.sqlite.entities.pets import PetsTable

from .pets_repository import PetsRepository


class MockConnection:
    def __init__(self) -> None:
        self.session = Mock()

        self.session.scalars.return_value.all.return_value = [
            PetsTable(id=1, name="dom", type="dog"),
            PetsTable(id=2, name="orange", type="cat"),
        ]

        self.session.scalar.return_value = PetsTable(
            id=1,
            name="dog",
            type="dog",
        )

    def __enter__(self):
        return self.session

    def __exit__(self, exc_type, exc, tb):
        pass


def test_list_pets():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)

    response = repo.list_pets()

    mock_connection.session.scalars.assert_called_once()

    assert response[0].name == "dom"
    assert response[1].name == "orange"


def test_delete_pet():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)

    response = repo.delete_pet(1)

    mock_connection.session.scalar.assert_called_once()
    mock_connection.session.delete.assert_called_once()
    mock_connection.session.commit.assert_called_once()

    assert response is True


def test_delete_pet_not_found():
    mock_connection = MockConnection()
    mock_connection.session.scalar.return_value = None

    repo = PetsRepository(mock_connection)

    response = repo.delete_pet(3)

    assert response is False

    mock_connection.session.delete.assert_not_called()
    mock_connection.session.commit.assert_not_called()
