#fastapi
from fastapi.testclient import TestClient
from fastapi import status

from .main import app

#datos de prueba
from .enums import data_vacante as data

client = TestClient(app)

def test_create_vancancy():
    """ 
    Test para probar que se puede guardar 
    una vacante satisfactoriamente. 
    """
    response = client.post("/vacantes/", json=data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == data

def test_get_all_vancancies():
    """  
    Test para probar que
    se listen las vacantes.
    """
    response = client.get("/vacantes")
    assert response.status_code == status.HTTP_200_OK
    assert data in response.json()

def test_update_vacancy_successful():
    """
    Test para actualizar una vacante exitosamente.
    """
    response = client.put(
    '/vacantes/c09f1301-7dbb-494f-a16f-91324083434a', 
    json={
        "PositionName": "Java Dev", 
        "CompanyName": "Microsoft", 
        "Salary": 2500, 
        "Currency":"USD",
        "VacancyLink":"www.microsoft.com", 
        "RequiredSkills":[{"Java": 5},{"Mysql": 6}]
        }
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "message": "La vacante ha sido actualizada satisfactoriamente"
    }

def test_delete_vacancy_successful():
    """
    Test para eliminar una vacante
    exitosamente.
    """
    response = client.delete(
        '/vacantes/c09f1301-7dbb-494f-a16f-91324083434a'
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "message":"La vacante ha sido eliminada satisfactoriamente"
    }

def test_update_vacancy__invalid_id():
    """
    Test para probar que si se pasa por parametro
    un id diferente la aplicacion devuelve un status code 404
    y no permite actualizar la vacante.
    """
    response = client.put(
    '/vacantes/c09f1301-7dbb-494f-a16f-9132408343',
    json={
        "PositionName": "Java Dev", 
        "CompanyName": "Microsoft", 
        "Salary": 2500, 
        "Currency":"USD",
        "VacancyLink":"www.microsoft.com", 
        "RequiredSkills":[{"Java": 5},{"Mysql": 6}]
        }
    )
    assert response.json()['status_code'] == status.HTTP_404_NOT_FOUND
    assert response.json()['detail'] == "No se pudo actualizar la vacante"
    
def test_delete_vacancy__invalid_id():
    """
    Test para probar que si se pasa por parametro
    un id diferente la aplicacion devuelve un status code 404
    y no permite eliminar la vacante.
    """
    response = client.delete('/vacantes/c09f1301-7dbb-494f-a16f-9132408343')
    assert response.json()['status_code'] == status.HTTP_404_NOT_FOUND
    assert response.json()['detail'] == "No se pudo eliminar la vacante"
