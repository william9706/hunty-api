from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# usuario model

class Usuarios(BaseModel):
    UserId: Optional[str]
    FirstName: str = Field(..., max_Length = 75)
    LastName: str = Field(max_Length = 75)
    Email:EmailStr = Field(..., max_Length = 30)
    YearsPreviousExperience: int 
    Skills: list = []