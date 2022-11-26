#fastapi
from fastapi.testclient import TestClient
from fastapi import status

from .main import app

#datos de prueba
from .enums import data_empresa as data

client = TestClient(app)

def test_create_company():
    """ 
    Test para probar que se puede guardar 
    una empresa satisfactoriamente. 
    """
    response = client.post("/empresas/", json=data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == data

def test_get_all_company():
    """  
    Test para probar que
    se listen las empresas.
    """
    response = client.get("/empresas")
    assert response.status_code == status.HTTP_200_OK
    assert data in response.json()

def test_update_company_successful():
    """
    Test para actualizar una empresa exitosamente.
    """
    response = client.put(
    '/empresas/f39d1342-8ddc-168g-s10f-24754283484a', 
    json={
        "CompanyName":"Hunty",
        "Sector":"tecnología",
        "Email":"hunty@gmail.com",
        "Web":"www.hunty.com",
        "Employees":300
        }
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "message": "La empresa ha sido actualizada satisfactoriamente"
    }

def test_delete_company_successful():
    """
    Test para eliminar una empresa
    exitosamente.
    """
    response = client.delete(
        '/empresas/f39d1342-8ddc-168g-s10f-24754283484a'
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "message":"La empresa ha sido eliminada satisfactoriamente"
    }

def test_update_company__invalid_id():
    """
    Test para probar que si se pasa por parametro
    un id diferente la aplicacion devuelve un status code 404
    y no permite actualizar la empresa.
    """
    response = client.put(
    '/empresas/f39d1342-8ddc-168g-s10f-24754283484a',
    json={
        "CompanyName":"Tiqal",
        "Sector":"tecnología",
        "Email":"Tiqal@gmail.com",
        "Web":"www.Tiqal.com",
        "Employees":150
        }
    )
    assert response.json()['status_code'] == status.HTTP_404_NOT_FOUND
    assert response.json()['detail'] == "No se pudo actualizar la empresa"
    
def test_delete_company__invalid_id():
    """
    Test para probar que si se pasa por parametro
    un id diferente la aplicacion devuelve un status code 404
    y no permite eliminar la empresa.
    """
    response = client.delete('/empresas/f39d1342-8ddc-168g-s10f-24754283484a')
    assert response.json()['status_code'] == status.HTTP_404_NOT_FOUND
    assert response.json()['detail'] == "No se pudo eliminar la empresa"
