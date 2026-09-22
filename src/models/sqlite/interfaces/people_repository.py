from abc import ABC, abstractmethod

from src.models.sqlite.dto.person_with_pet import PersonWithPet


class PeopleRepositoryInterface(ABC):
    @abstractmethod
    def insert_person(
        self, first_name: str, last_name: str, age: int, pet_id: int
    ) -> None:
        pass

    @abstractmethod
    def get_person(self, person_id: int) -> PersonWithPet | None:
        pass
