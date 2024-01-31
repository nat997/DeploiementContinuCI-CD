import pytest
from .. import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Degree Data' in response.data
    assert b'Timestamp Data' in response.data

# You can add more test cases as needed.
