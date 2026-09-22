from dataclasses import dataclass


@dataclass
class PersonWithPet:
    id: int
    first_name: str
    last_name: str
    age: int
    pet_name: str | None
    pet_type: str | None
