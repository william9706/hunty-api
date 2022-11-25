from pydantic import BaseModel, EmailStr, Field
from typing import Optional


# vacante model
class Empresas(BaseModel):  
    Id: Optional[str]
    CompanyName:str = Field(..., max_Length = 50)
    Sector:str = Field(max_Length = 25)
    Email:EmailStr = Field(..., max_Length = 30)
    Web:str = Field(max_Length = 25)
    Employees:int
