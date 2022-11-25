from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)




def test_validar_prueba():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message":"Bienvenido a la api de hunty"}



def test_read_item():
    response = client.get("/items/foo", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert response.json() == {
        "id": "foo",
        "title": "Foo",
        "description": "There goes my hero",
    }