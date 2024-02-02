import pytest
from unittest.mock import patch
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as test_client:
        yield test_client

@patch('app.fetch_degree_data')
def test_degree_page(mock_fetch_degree_data, client):
    # Mock the database response for degree data
    mock_fetch_degree_data.return_value = [[1, 10.5], [2, 20.7]]

    # Make a request to the Flask app for the degree endpoint
    response = client.get('/degree')

    # Check if the status code is 200 (OK)
    assert response.status_code == 200

    # Convert the response data to JSON and perform checks
    json_data = response.get_json()
    assert json_data['Degree Data'] == [[1, 10.5], [2, 20.7]]

@patch('app.fetch_timestamp_data')
def test_timestamp_page(mock_fetch_timestamp_data, client):
    # Mock the database response for timestamp data
    mock_fetch_timestamp_data.return_value = [[1, '2021-01-01 00:00:00'], [2, '2021-01-02 00:00:00']]

    # Make a request to the Flask app for the timestamp endpoint
    response = client.get('/timestamp')

    # Check if the status code is 200 (OK)
    assert response.status_code == 200

    # Convert the response data to JSON and perform checks
    json_data = response.get_json()
    assert json_data['Timestamp Data'] == [[1, '2021-01-01 00:00:00'], [2, '2021-01-02 00:00:00']]
