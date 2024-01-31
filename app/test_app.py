import pytest
from app import app

@pytest.fixture
def test_flask_api():
    url = 'http://localhost:5000'  # Replace with your Flask API URL
    response = requests.get(url)
    assert response.status_code == 200  # Assuming a successful response code is 200 OK


