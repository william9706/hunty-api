from pydantic import BaseModel, EmailStr, Field
from typing import Optional


# vacante model
class Vacantes(BaseModel):  
    PositionName:str = Field(..., max_Length = 50)
    CompanyName:str = Field(..., max_Length = 35)
    Salary:int = Field(...)
    Currency:str = Field(..., min_Length = 3, max_Length = 25)
    VacancyId: Optional[str]
    VacancyLink:str = Field(max_Length = 50)
    RequiredSkills: list = []
