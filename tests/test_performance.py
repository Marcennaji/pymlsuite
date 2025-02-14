import time
from requests import get


def test_api_performance():
    start = time.time()
    response = get("http://127.0.0.1:8000/predict")
    assert response.status_code == 200
    assert time.time() - start < 1.0
