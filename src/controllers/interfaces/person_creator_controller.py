from abc import ABC, abstractmethod

from src.schemas.create_person_schema import CreatePersonSchema


class PersonCreatorControllerInterface(ABC):
    @abstractmethod
    def create_person(self, person_data: CreatePersonSchema) -> dict:
        pass
