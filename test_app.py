from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200

def test_not_found():
    client = app.test_client()
    response = client.get("/rota-invalida")
    assert response.status_code == 404

def test_method_not_allowed():
    client = app.test_client()
    response = client.post("/")
    assert response.status_code in [405, 404]

def test_response_content():
    client = app.test_client()
    response = client.get("/")
    assert response.data is not None
    