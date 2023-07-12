from datetime import datetime

import pytest
from fastapi.testclient import TestClient

from app.database import SessionLocal, get_db
from app.main import app
from app.schemas import User


# Override the dependency function to use an in-memory SQLite database for testing
def get_test_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="module")
def test_client():
    """
    Use the TestClient provided by FastAPI to simulate HTTP requests
    """

    with TestClient(app) as client:
        yield client


def test_create_user(test_client: TestClient, monkeypatch):
    """
    Simulate a successful POST request to create a user
    """

    user_data = {
        "id": 1,
        "last_seen": datetime.utcnow().isoformat(),
        "created_at": datetime.utcnow().isoformat(),
        "is_active": True,
        "access_token": "test_token"
    }
    monkeypatch.setattr("app.main.user_ops.create_user", lambda db: User(**user_data))

    response = test_client.post("/users/", json=user_data)
    assert response.status_code == 200
    assert response.json() == user_data


def test_read_users(test_client: TestClient, monkeypatch):
    """
    Simulate a successful GET request to read a list of users
    """

    users = [
        {
            "id": 1,
            "last_seen": datetime.utcnow(),
            "created_at": datetime.utcnow(),
            "is_active": True,
            "access_token": "test_token"
        },
        {
            "id": 2,
            "last_seen": datetime.utcnow(),
            "created_at": datetime.utcnow(),
            "is_active": False,
            "access_token": "test_token"
        }
    ]
    monkeypatch.setattr("app.main.user_ops.get_users", lambda db, skip, limit: [User(**user) for user in users])

    response = test_client.get("/users/")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_read_user(test_client: TestClient, monkeypatch):
    """
    Simulate a successful GET request to read a user
    """

    user_data = {
        "id": 1,
        "last_seen": datetime.utcnow(),
        "created_at": datetime.utcnow(),
        "is_active": True,
        "access_token": "test_token"
    }
    monkeypatch.setattr("app.main.user_ops.get_user", lambda db, user_id: User(**user_data))

    response = test_client.get("/users/1")
    assert response.status_code == 200
    assert response.json()['id'] == 1


def test_read_user_not_found(test_client: TestClient, monkeypatch):
    """
    Simulate a GET request to read a user that doesn't exist
    """

    monkeypatch.setattr("app.main.user_ops.get_user", lambda db, user_id: None)

    response = test_client.get("/users/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "The requested resource could not be found on the server."}


def test_read_root(test_client: TestClient, monkeypatch):
    """
    Simulate a GET request to read health information
    """

    monkeypatch.setattr("app.main.table_ops.total_rows", lambda db: 100)
    monkeypatch.setattr("app.main.table_ops.total_tables", lambda: 5)

    response = test_client.get("/health")
    assert response.status_code == 200
    response_data = response.json()
    assert "timestamp" in response_data
    assert "status" in response_data
    assert "database" in response_data
    assert response_data["status"] == "OK"
    assert response_data["database"]["totalRows"] == 100
    assert response_data["database"]["totalTables"] == 5


@pytest.fixture(scope="module", autouse=True)
def override_dependencies():
    """
    Override the get_db function to use the test database
    """

    app.dependency_overrides[get_db] = get_test_db

    yield

    # Clean up the dependency override
    del app.dependency_overrides[get_db]
