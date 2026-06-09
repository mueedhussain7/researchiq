"""
Smoke tests — API starts and core endpoints respond correctly.
These run first in CI and must always pass.
"""


def test_health_returns_200(client):
    assert client.get("/health").status_code == 200


def test_health_body(client):
    data = client.get("/health").json()
    assert data["status"] == "healthy"
    assert data["app"] == "ResearchIQ"
    assert "version" in data
    assert "env" in data


def test_root_returns_200(client):
    assert client.get("/").status_code == 200


def test_root_has_docs_link(client):
    data = client.get("/").json()
    assert data["docs"] == "/docs"
    assert "ResearchIQ" in data["message"]


def test_openapi_schema_loads(client):
    response = client.get("/openapi.json")
    assert response.status_code == 200
    assert "openapi" in response.json()
