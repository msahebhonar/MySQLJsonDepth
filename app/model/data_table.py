from sqlalchemy import JSON
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from app.setup import get_engine


class Base(DeclarativeBase):
    pass


class DataTable(Base):
    __tablename__ = "data_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    data: Mapped[dict] = mapped_column(JSON)

    def __init__(self, data: dict) -> None:
        self.data = data


Base.metadata.drop_all(bind=get_engine())
Base.metadata.create_all(bind=get_engine())
