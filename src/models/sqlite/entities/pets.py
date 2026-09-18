from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.models.sqlite.settings.base import Base


class PetsTable(Base):
    __tablename__ = "pets"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    type: Mapped[str] = mapped_column(String, nullable=False)

    def __repr__(self):
        return f"Pets [name={self.name}, type={self.type}]"
