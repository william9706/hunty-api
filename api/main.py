#fast API
from fastapi import FastAPI, HTTPException
import uvicorn

#python
from datetime import datetime
from uuid import uuid4 as uuid

#pydantic
from pydantic import BaseModel, EmailStr, Field

#typing
from typing import Optional

 ##### MODELS ###### 
 
# empresa model
class Empresas(BaseModel):  
    Id: Optional[str]
    CompanyName:str = Field(..., max_Length = 50)
    Sector:str = Field(max_Length = 25)
    Email:EmailStr = Field(..., max_Length = 30)
    Web:str = Field(max_Length = 25)
    Employees:int

# usuario model
class Usuarios(BaseModel):
    UserId: Optional[str]
    FirstName: str = Field(..., max_Length = 75)
    LastName: str = Field(max_Length = 75)
    Email:EmailStr = Field(..., max_Length = 30)
    YearsPreviousExperience: int 
    Skills: list = []


# vacante model
class Vacantes(BaseModel):  
    PositionName:str = Field(..., max_Length = 50)
    CompanyName:str = Field(..., max_Length = 35)
    Salary:int = Field(...)
    Currency:str = Field(..., min_Length = 3, max_Length = 25)
    VacancyId: Optional[str]
    VacancyLink:str = Field(max_Length = 50)
    RequiredSkills: list = []


app = FastAPI()

vacantes = []
usuarios = []
empresas = []

##### VACANTES ######
@app.get('/')
def index():
    return {"message":"Bienvenido a la api de hunty"}

@app.get('/vacantes')
def get_vacantes():
    """
    Fuinción para listar vacantes.
    """
    return vacantes

@app.post('/vacantes')
def save_vacante(vacante: Vacantes):
    """ 
    Función para guardar vacantes en el arreglo vacantes.
    @param vacante: objeto vacante de tipo Vacante
    @returns: retornar un diccionario
    @rtype: dict
    """
    vacante.VacancyId = str(uuid())
    vacantes.append(vacante.dict())
    return vacantes[-1]

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
                    "message":"La vacante ha sido eliminada satisfactoriamente."
                }

    return HTTPException(
        status_code=404, 
        detail="No se pudo eliminar la vacante."
    )

@app.put('/vacantes/{vacante_id}')
def update_vacante(vacante_id: str, updatedVacante: Vacantes):
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
                "message":"La vacante ha sido actualizada satisfactoriamente."
            }
    return HTTPException(
        status_code=404, 
        detail="No se pudo actualizar la vacante."
    )


##### USUARIOS ###### 
@app.get('/usuarios')
def get_usuarios():
    """
    Fuinción para listar usuarios.
    """
    return usuarios

@app.post('/usuarios')
def save_usuario(usuario: Usuarios):
    """ 
    Función para guardar usuarios en el arreglo usuarios.
    @param usuario: objeto usuario de tipo Usuario
    @returns: retornar un diccionario con el objeto de usuario que se agrega
    @rtype: dict
    """
    usuario.UserId = str(uuid())
    usuarios.append(usuario.dict())
    return usuarios[-1]

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
def update_usuario(usuario_id: str, updatedUsuario: Usuarios):
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


##### EMPRESAS ######
@app.get('/empresas')
def get_empresas():
    """
    Fuinción para listar empresas.
    """
    return empresas

@app.post('/empresas')
def save_usuario(empresa: Empresas):
    """ 
    Función para guardar empresas en el arreglo empresas.
    @param empresa: objeto empresa de tipo Empresa
    @returns: retornar un json con los datos de la empresa creada
    @rtype: json
    """
    empresa.Id = str(uuid())
    empresas.append(empresa.dict())
    return empresas[-1]

@app.delete('/empresas/{empresa_id}')
def delete_empresa(empresa_id: str):
    """ 
    Función para eliminar una empresa especifica.
    @param empresa_id: uuid de una empresa
    @returns: Respuesta de la api llamada.
    """
    for index, empresa in enumerate(empresas):
        if  empresa['Id'] == empresa_id:
                empresas.pop(index)
                return {
                    "message":"La empresa ha sido eliminada satisfactoriamente."
                }

    return HTTPException(
        status_code=404, 
        detail="No se pudo eliminar la empresa."
    )

@app.put('/empresas/{empresa_id}')
def update_empresa(empresa_id: str, updatedEmpresa: Empresas):
    """
    Función para actualizar una empresa.
    @param empresa_id: uuid de una empresa
    @param updatedEmpresa: objeto empresa que se va a actualizar.
    @return: Respuesta de la api llamada.
    """
    for index, empresa in enumerate(empresas):
        if  empresa['Id'] == empresa_id:
            empresas[index]['CompanyName'] = updatedEmpresa.CompanyName
            empresas[index]['Sector'] = updatedEmpresa.Sector
            empresas[index]['Email'] = updatedEmpresa.Email
            empresas[index]['Web'] = updatedEmpresa.Web
            empresas[index]['Employees'] = updatedEmpresa.Employees
            return {
                "message":"La empresa ha sido actualizada satisfactoriamente."
            }
    return HTTPException(
        status_code=404, 
        detail="No se pudo actualizar la empresa."
    )
