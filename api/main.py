from fastapi import FastAPI, HTTPException
from datetime import datetime
from uuid import uuid4 as uuid
import uvicorn
#models
from models.vacante import Vacante
from models.usuario import Usuario

app = FastAPI()

vacantes = []

usuarios = []


@app.get('/')
def index():
    return {"welcome":"Bienvenido a la api de hunty"}

@app.get('/vacantes')
def get_vacantes():
    """
    Fuinción para listar vacantes.
    """
    return vacantes

@app.post('/vacantes')
def save_vacante(vacante: Vacante):
    """ 
    Función para guardar vacantes en el arreglo vacantes.
    @param vacante: objeto vacante de tipo Vacante
    @returns: retornar un diccionario
    @rtype: dict
    """
    vacante.VacancyId = str(uuid())
    vacantes.append(vacante.dict())
    return vacantes[-1]

@app.get('/vacantes/{vacante_id}')
def get_vacante(vacante_id: str):
    """ 
    Función para traer listar un solo objeto por id de vacante..
    @param vacante_id: uuid de una vacante
    """
    for vacante in vacantes:
        if  vacante['VacancyId'] == vacante_id:
                return vacante

    raise HTTPException(
        status_code=404, 
        detail="La vacante no existe."
    )

@app.delete('/vacantes/{vacante_id}')
def delete_vacante(vacante_id: str):
    """ 
    Función para eliminar una vacante especifica.
    @param vacante_id: uuid de una vacante
    @returns: Respuesta de la api llamada.
    """
    for index, vacante in enumerate(vacantes):
        if  vacante['VacancyId'] == vacante_id:
                vacantes.pop(index)
                return {
                    "message":"La vacante ah sido eliminada satisfactoriamente."
                }

    return HTTPException(
        status_code=404, 
        detail="No se pudo eliminar la vacante."
    )

@app.put('/vacantes/{vacante_id}')
def update_vacante(vacante_id: str, updatedVacante: Vacante):
    """
    Función para actualizar una vacante.
    @param vacante_id: uuid de una vacante
    @param updatedVacante: objeto vacante que se va a actualizar.
    @return: Respuesta de la api llamada.
    """
    for index, vacante in enumerate(vacantes):
        if  vacante['VacancyId'] == vacante_id:
            vacantes[index]['PositionName'] = updatedVacante.PositionName
            vacantes[index]['CompanyName'] = updatedVacante.CompanyName
            vacantes[index]['Salary'] = updatedVacante.Salary
            vacantes[index]['Currency'] = updatedVacante.Currency
            vacantes[index]['VacancyLink'] = updatedVacante.VacancyLink
            vacantes[index]['RequiredSkills'] = updatedVacante.RequiredSkills
            return {
                "message":"La vacante ah sido actualizada satisfactoriamente."
            }
    return HTTPException(
        status_code=404, 
        detail="No se pudo actualizar la vacante."
    )

    
@app.get('/usuarios')
def get_usuarios():
    """
    Fuinción para listar usuarios.
    """
    return usuarios

@app.post('/usuarios')
def save_usuario(usuario: Usuario):
    """ 
    Función para guardar usuarios en el arreglo usuarios.
    @param usuario: objeto usuario de tipo Usuario
    @returns: retornar un diccionario con el objeto de usuario que se agrega
    @rtype: dict
    """
    usuario.UserId = str(uuid())
    usuarios.append(usuarios.dict())
    return usuarios[-1]

@app.get('/usuarios/{usuario_id}')
def get_usuario(usuario_id: str):
    """ 
    Función para listar un solo objeto por id de usuario.
    @param usuario_id: uuid de un usuario
    """
    for usuario in usuarios:
        if  usuario['UserId'] == usuario_id:
                return usuario

    raise HTTPException(
        status_code=404, 
        detail="El usuario no existe."
    )

@app.delete('/usuarios/{usuario_id}')
def delete_usuario(usuario_id: str):
    """ 
    Función para eliminar un usuario especifico.
    @param usuario_id: uuid de un usuario
    @returns: Respuesta de la api llamada.
    """
    for index, usuario in enumerate(usuarios):
        if  usuario['UserId'] == usuario_id:
                usuarios.pop(index)
                return {
                    "message":"El usuario ha sido eliminado satisfactoriamente."
                }

    return HTTPException(
        status_code=404, 
        detail="No se pudo eliminar el usuario."
    )

@app.put('/usuarios/{usuario_id}')
def update_usuario(usuario_id: str, updatedUsuario: Usuario):
    """
    Función para actualizar un usuario.
    @param usuario_id: uuid de un usuario
    @param updatedUsuario: objeto usuario que se va a actualizar.
    @return: Respuesta de la api llamada.
    """
    for index, usuario in enumerate(usuarios):
        if  usuario['UserId'] == usuario_id:
            usuarios[index]['FirstName'] = updatedUsuario.FirstName
            usuarios[index]['LastName'] = updatedUsuario.LastName
            usuarios[index]['Email'] = updatedUsuario.Email
            usuarios[index]['YearsPreviousExperience'] = updatedUsuario.YearsPreviousExperience
            usuarios[index]['Skills'] = updatedUsuario.Skills
            return {
                "message":"El usuario ha sido actualizado satisfactoriamente."
            }
    return HTTPException(
        status_code=404, 
        detail="No se pudo actualizar el usuario."
    )