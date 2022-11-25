from pydantic import BaseModel, EmailStr, Field
from typing import Optional

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
