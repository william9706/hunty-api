from pydantic import BaseModel, EmailStr
from typing import Optional


# vacante model
class Vacante(BaseModel):  
    PositionName:str
    CompanyName:str
    Salary:int
    Currency:str
    VacancyId: Optional[str]
    VacancyLink:str
    RequiredSkills: list = []

