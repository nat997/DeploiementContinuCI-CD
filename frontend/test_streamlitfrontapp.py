import pytest
from streamlitfrontapp import fetch_data, process_data

def test_fetch_data():
    # Test that data is fetched correctly
    api_url = "http://localhost:5000/"
    data = fetch_data(api_url)
    assert "Degree Data" in data and "Timestamp Data" in data

def test_process_data():
    # Mock data similar to what your API would return
    mock_data = {
        "Degree Data": [[1, 20], [2, 30]],
        "Timestamp Data": [[1, "2021-01-01 00:00:00"], [2, "2021-01-02 00:00:00"]]
    }
    degree_data, timestamp_data = process_data(mock_data)
    assert not degree_data.empty
    assert not timestamp_data.empty
