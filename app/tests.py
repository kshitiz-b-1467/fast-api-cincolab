import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.const import  STATUS
 
@pytest.fixture(scope="module")
def test_client():
    """
    Use the TestClient provided by FastAPI to simulate HTTP requests
    """

    with TestClient(app) as client:
        yield client


def test_read_root(test_client: TestClient):
    """
    Simulate a GET request to read health information
    """

    response = test_client.get("/health")
    assert response.status_code == 200
    response_data = response.json()
    assert "timestamp" in response_data
    assert "status" in response_data
    assert response_data['status'] == STATUS.HTTP_200_OK['message']
    