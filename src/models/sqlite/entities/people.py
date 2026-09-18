from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from src.models.sqlite.settings.base import Base


class PeopleTable(Base):
    __tablename__ = "people"

    id: Mapped[int] = mapped_column(primary_key=True)

    first_name: Mapped[str] = mapped_column(String(100), nullable=False)

    last_name: Mapped[str] = mapped_column(String(100), nullable=False)

    age: Mapped[int] = mapped_column(nullable=False)

    pet_id: Mapped[int] = mapped_column(ForeignKey("pets.id"))

    def __repr__(self):
        return (
            f"People [first_name={self.first_name}, "
            f"last_name={self.last_name}, "
            f"age={self.age}, "
            f"pet_id={self.pet_id}]"
        )
