import pytest
from app import app as flask_app

@pytest.fixture
def client():
    """Create a clean, isolated test client instance for the Flask application."""
    with flask_app.test_client() as client:
        yield client

def test_home_route_renders_dashboard(client):
    """Verify that the home page loads successfully with the UI HTML code."""
    response = client.get('/')
    assert response.status_code == 200
    # Ensure the dashboard title exists in the returned UI document
    assert b"DevSecOps Secure Dashboard" in response.data

def test_greet_route_sanitization(client):
    """Verify that the backend greet endpoint responds with the correct sanitized JSON framework."""
    response = client.get('/greet?name=Papi')
    assert response.status_code == 200
    # Assert JSON payload key match
    assert response.json["message"] == "Hello, Papi! This request was sanitized and validated."
