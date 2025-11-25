from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_create_resource_and_returns_200():
    response = client.post("/resources/", json={"url": "https://google.com"})
    assert response.status_code == 200
    assert response.json() == {"url": "https://google.com"}