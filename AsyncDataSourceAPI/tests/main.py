import sys

sys.path.append("/path/to/your/project")
import json
import asyncio
import pytest
from fastapi.testclient import TestClient
from AsyncDataSourceAPI.main import app, get_data_from_db


client = TestClient(app)


@pytest.fixture
def mocker():
    from unittest.mock import Mock

    return Mock()


def test_get_data_ignore_error(mocker):
    mock_connect = mocker.patch("aiosqlite.connect")

    mock_cursor = mocker.AsyncMock()
    mocker.patch("aiosqlite.connection.Connection.execute", return_value=mock_cursor)

    response = client.get("/data")

    assert response.status_code == 200

    expected_result = [
        {"id": 1, "name": "Data 1-1"},
        {"id": 2, "name": "Data 1-2"},
        {"id": 12, "name": "Data 2-1"},
        {"id": 15, "name": "Data 2-2"},
        {"id": 22, "name": "Data 3-1"},
        {"id": 25, "name": "Data 3-2"},
        {"id": 32, "name": "Data 1-32"},
        {"id": 45, "name": "Data 2-3"},
        {"id": 55, "name": "Data 3-3"},
    ]

    assert response.json() == expected_result


def test_get_data_timeout_error(mocker, monkeypatch):
    async def mock_wait_for(func, timeout):
        raise asyncio.TimeoutError("Timeout error")

    monkeypatch.setattr(asyncio, "wait_for", mock_wait_for)

    response = client.get("/data")

    assert response.status_code == 200

    expected_result = []
    assert response.json() == expected_result
