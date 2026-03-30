from app import app


def test_soma():
    client = app.test_client()
    response = client.get("/soma/2/3")
    assert response.status_code == 200
    assert response.json["resultado"] == 5


def test_subtracao():
    client = app.test_client()
    response = client.get("/subtracao/5/2")
    assert response.status_code == 200
    assert response.json["resultado"] == 3
