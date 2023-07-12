from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    """
    User model schema
    """

    id: int
    created_at: datetime
    last_seen: datetime
    is_active: bool
    access_token: str

    class Config:
        from_attributes = True
