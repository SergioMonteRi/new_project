from abc import ABC, abstractmethod


class PetListControllerInterface(ABC):
    @abstractmethod
    def list_pets(self) -> dict:
        pass
