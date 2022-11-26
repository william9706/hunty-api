from fastapi.testclient import TestClient
from .main import app
from .enums import vacante, vacante_2
import json

client = TestClient(app)

def test_list_vancancy_successful():
    """  
    Test para probar que
    se listen las vacantes
    """
    response = client.get('/vacantes')
    assert response.status_code == 200

def test_save_vancancy_successful():
    """ 
    Test para probar que se puede guardar 
    una vacante satisfactoriamente. 
    """
    response = client.post(
        "/vacantes", 
        json=vacante
    )
    data = response.json()
    assert response.status_code == 200
    assert data["PositionName"] == "Python Dev"
    assert data == vacante

def test_update_vacancy_successful():

    response = client.put(
    '/vacantes/ec03955b-3fd8-4261-9eba-1e60b85f5014/', 
    json=vacante_2
    )
    assert response.status_code == 200
    assert response.json() == vacante_2
