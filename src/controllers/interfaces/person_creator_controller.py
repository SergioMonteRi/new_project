from abc import ABC, abstractmethod


class PersonCreatorControllerInterface(ABC):
    @abstractmethod
    def create_person(self, person_data: dict) -> dict:
        pass
