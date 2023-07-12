from datetime import datetime
from fastapi import FastAPI
from app.const import UTC_DATE_TIME_FORMAT, STATUS
from app.utils import health_check_response

app = FastAPI()


@app.get("/health/")
def read_root():
    """
    Return health check response
    """

    current_time = datetime.utcnow()
    timestamp = current_time.strftime(UTC_DATE_TIME_FORMAT)

    return health_check_response(
        status=STATUS.HTTP_200_OK["message"],
        timestamp=timestamp,
    )
