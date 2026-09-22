from abc import ABC, abstractmethod


class PetDeleteControllerInterface(ABC):
    @abstractmethod
    def delete_pet(self, pet_id: int) -> bool:
        pass
