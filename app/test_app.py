import pytest
import app  
from unittest.mock import patch

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

@patch('app.fetch_degree_data')
@patch('app.fetch_timestamp_data')
def test_index(mock_fetch_timestamp_data, mock_fetch_degree_data, client):
    mock_fetch_degree_data.return_value = [(1, 25.5), (2, 30.7)]
    mock_fetch_timestamp_data.return_value = [(1, '2021-01-01 00:00:00'), (2, '2021-01-02 00:00:00')]

    response = client.get('/')
    assert response.status_code == 200
    assert 'Degree Data' in response.json
    assert 'Timestamp Data' in response.json
    assert response.json['Degree Data'] == [(1, 25.5), (2, 30.7)]
    assert response.json['Timestamp Data'] == [(1, '2021-01-01 00:00:00'), (2, '2021-01-02 00:00:00')]
