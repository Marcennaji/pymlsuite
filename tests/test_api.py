import requests


def test_api_response():
    response = requests.get("http://127.0.0.1:8000/predict?data=test")
    assert response.status_code == 200
