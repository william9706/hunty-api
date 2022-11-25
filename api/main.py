from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from uuid import uuid4 as uuid
from typing import Optional
import uvicorn

app = FastAPI()

vacantes = []

# vacante model
class Vacante(BaseModel):  
    PositionName:str
    CompanyName:str
    Salary:int
    Currency:str
    VacancyId: Optional[str]
    VacancyLink:str
    RequiredSkills: list = []


@app.get('/')
def read_root():
    return {"welcome":"welcome to my api"}

@app.get('/vacantes')
def get_vacantes():
    return vacantes

@app.post('/vacantes')
def save_vacante(vacante: Vacante):
    """ 
    Función para guardar vacentes en el arreglo vacantes. 
    """
    vacante.VacancyId = str(uuid())
    vacantes.append(vacante.dict())
    return vacantes[-1]

@app.get('/vacantes/{vacante_id}')
def get_vacante(vacante_id: str):
    """ 
    Función para listar un solo objeto busacndo por id. 
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
    """
    for index, vacante in enumerate(vacantes):
        if  vacante['VacancyId'] == vacante_id:
            vacantes[index]['PositionName'] = updatedVacante.PositionName
            vacantes[index]['CompanyName'] = updatedVacante.CompanyName
            vacantes[index]['Salary'] = updatedVacante.Salary
            vacantes[index]['Currency'] = updatedVacante.Currency
            vacantes[index]['VacancyLink'] = updatedVacante.VacancyLink
            return {
                "message":"La vacante ah sido actualizada satisfactoriamente."
            }
    return HTTPException(
        status_code=404, 
        detail="No se pudo actualizar la vacante."
    )

