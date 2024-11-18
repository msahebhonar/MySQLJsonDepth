from sqlalchemy.orm import Session

from app.model.data_table import DataTable


def add_and_commit(session: Session, data: dict) -> None:
    row = DataTable(data)
    session.add(row)
    session.commit()
