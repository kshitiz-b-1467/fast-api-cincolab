import os

from dotenv import load_dotenv

from app.utils import HttpStatus

load_dotenv()

STATUS = HttpStatus()

DEFAULT_LIMIT = 100
DEFAULT_SKIP = 0

SQLALCHEMY_DATABASE_URL_DEV = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = os.environ.get(
    "DATABASE_URL", SQLALCHEMY_DATABASE_URL_DEV
).replace("postgres://", "postgresql://")
UTC_DATE_TIME_FORMAT = "%Y-%m-%d %H:%M:%S UTC"
