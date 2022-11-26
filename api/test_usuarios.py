from fastapi.testclient import TestClient
from .main import app
from .enums import data_usuario as data

client = TestClient(app)

def test_create_user():
    """ 
    Test para guardar un usuario 
    satisfactoriamente. 
    """
    response = client.post("/usuarios/", json=data)
    assert response.status_code == 200
    assert response.json() == data

def test_get_all_users():
    """  
    Test para probar que
    se listen los usuaior creados.
    """
    response = client.get("/usuarios")
    assert response.status_code == 200
    assert data in response.json()

def test_update_user_successful():
    """
    Test para actualizar un usuario exitosamente.
    """
    response = client.put(
    '/usuarios/a09f1400-7dcc-018f-a16f-94754083434a', 
    json={
        "FirstName": "Camilo",
        "LastName": "Gutierrez",
        "Email": "camilo02@gmail.com",
        "YearsPreviousExperience": 2,
        "Skills": [
                {
                    "Python": 7
                },
                {
                    "NoSQL": 3
                },
            ]
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "message": "El usuario ha sido actualizado satisfactoriamente"
    }

def test_delete_user_successful():
    """
    Test para eliminar un usuario
    exitosamente.
    """
    response = client.delete(
        '/usuarios/a09f1400-7dcc-018f-a16f-94754083434a'
    )
    assert response.status_code == 200
    assert response.json() == {
        "message":"El usuario ha sido eliminado satisfactoriamente"
    }

def test_update_user__invalid_id():
    """
    Test para probar que si se pasa por parametro
    un id diferente la aplicacion devuelve un status code 404
    y no permite actualizar el usuario.
    """
    response = client.put(
    '/usuarios/c09f1301-7dbb-494f-a16f-8888408343',
    json={
        "FirstName": "Camilo",
        "LastName": "Gutierrez",
        "Email": "camilo02@gmail.com",
        "YearsPreviousExperience": 2,
        "Skills": [
                {
                    "Python": 7
                },
                {
                    "NoSQL": 3
                },
            ]
        }
    )
    assert response.json()['status_code'] == 404
    assert response.json()['detail'] == "No se pudo actualizar el usuario"
    
def test_delete_user__invalid_id():
    """
    Test para probar que si se pasa por parametro
    un id diferente la aplicacion devuelve un status code 404
    y no permite eliminar el usuario.
    """
    response = client.delete('/usuarios/c09f1301-7dbb-494f-a16f-8888408343')
    assert response.json()['status_code'] == 404
    assert response.json()['detail'] == "No se pudo eliminar el usuario"
