"""Shared pytest fixtures available to all test files."""
import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.core.config import settings


@pytest.fixture(scope="session")
def test_settings():
    return settings


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c
