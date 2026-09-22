from abc import ABC, abstractmethod


class PersonFinderControllerInterface(ABC):
    @abstractmethod
    def find_person_by_id(self, person_id: int) -> dict:
        pass
