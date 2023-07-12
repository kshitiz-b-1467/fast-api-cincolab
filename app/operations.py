from sqlalchemy import MetaData, func
from sqlalchemy.orm import Session

from app import models
from app.const import DEFAULT_SKIP, DEFAULT_LIMIT
from app.database import engine

metadata = MetaData()
metadata.reflect(bind=engine)


class TableOperations:
    """
    Operations for all tables in the database
    """

    @staticmethod
    def delete_tables():
        metadata.drop_all(bind=engine)

    @staticmethod
    def total_tables():
        table_count = len(metadata.tables)
        return table_count

    @staticmethod
    def total_rows(db: Session):
        row_count = 0
        for table in metadata.sorted_tables:
            row_count += db.query(func.count()).select_from(table).scalar()

        return row_count


class UserOperations:
    """
    Operations for the User table
    """

    @staticmethod
    def get_user(db: Session, user_id: int):
        return db.query(models.User).filter(models.User.id == user_id).first()

    @staticmethod
    def get_users(db: Session, skip: int = DEFAULT_SKIP, limit: int = DEFAULT_LIMIT):
        return db.query(models.User).offset(skip).limit(limit).all()

    @staticmethod
    def create_user(db: Session):
        db_user = models.User()
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
