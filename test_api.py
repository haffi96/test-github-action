from fastapi.testclient import TestClient

from main import app

test_client = TestClient(app)


def test_hello():
    response = test_client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"Message": "Hello World!!"}
