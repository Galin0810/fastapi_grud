from starlette.testclient import TestClient

from app.main import app

client = TestClient(app)


@app.get("/ping")
def test_ping(test_app):
    response = test_app.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}
