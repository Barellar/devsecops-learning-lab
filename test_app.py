import pytest
from app import app as flask_app

@pytest.fixture
def client():
    with flask_app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json["status"] == "healthy"

def test_greet_route(client):
    response = client.get('/greet?name=Alice')
    assert response.status_code == 200
    assert response.json["message"] == "Hello, Alice!"
