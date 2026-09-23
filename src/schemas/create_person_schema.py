import re

from pydantic import BaseModel, Field, field_validator


class CreatePersonSchema(BaseModel):
    first_name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    age: int
    pet_id: int

    @field_validator("first_name", "last_name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        if not re.fullmatch(r"[a-zA-Z]+", value):
            raise ValueError("Name must contain only letters")

        return value
