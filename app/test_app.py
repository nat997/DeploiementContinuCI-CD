import pytest
from app import app

@pytest.fixture
def client():
    """Create a test client for the app."""
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_index_route(client):
    """Test the index route."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Degree Data' in response.data
    assert b'Timestamp Data' in response.data
