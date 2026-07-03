import pytest
import requests


@pytest.mark.duckduckgo
@pytest.mark.api
def test_duckduckgo_instant_answer_api():
    # Arrange: Setting up URL.
    URL = "https://jsonplaceholder.typicode.com/todos/1"

    # Act
    response = requests.get(url=URL, timeout=500)
    body = response.json()

    # Assert
    assert response.status_code == 200
    assert "delectus" in body["title"]
