from datetime import datetime

from sqlalchemy import Boolean, Column, Integer, String, DateTime

from app.database import Base


class User(Base):
    """
    Description: model for user table

    id: int
    last_seen: datetime
    created_at: datetime
    is_active: bool
    access_token: str

    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    last_seen = Column(DateTime, default=datetime.utcnow())
    created_at = Column(DateTime, default=datetime.utcnow())
    is_active = Column(Boolean, default=True)
    access_token = Column(String, default="")
