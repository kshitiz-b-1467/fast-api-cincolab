from datetime import datetime

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app import schemas, models
from app.const import DEFAULT_SKIP, DEFAULT_LIMIT, UTC_DATE_TIME_FORMAT, STATUS
from app.database import get_db, engine
from app.operations import TableOperations, UserOperations
from app.utils import health_check_response

app = FastAPI()

user_ops = UserOperations()
table_ops = TableOperations()
models.Base.metadata.create_all(bind=engine)


@app.post("/users/", response_model=schemas.User)
def create_user(db: Session = Depends(get_db)):
    """
    Create a new user
    """

    return user_ops.create_user(db=db)


@app.get("/users/", response_model=list[schemas.User])
def get_users(
    skip: int = DEFAULT_SKIP, limit: int = DEFAULT_LIMIT, db: Session = Depends(get_db)
):
    """
    Return list of users
    """

    users = user_ops.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}/", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    Return user by id
    """

    db_user = user_ops.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=STATUS.HTTP_404_NOT_FOUND["status_code"],
            detail=STATUS.HTTP_404_NOT_FOUND["detail"],
        )
    return db_user


@app.get("/health/")
def health_check_endpoint(db: Session = Depends(get_db)):
    """
    Return health check response
    """

    current_time = datetime.utcnow()
    timestamp = current_time.strftime(UTC_DATE_TIME_FORMAT)

    total_rows = table_ops.total_rows(db)
    total_tables = table_ops.total_tables()

    return health_check_response(
        status=STATUS.HTTP_200_OK["message"],
        timestamp=timestamp,
        total_rows=total_rows,
        total_tables=total_tables,
    )
