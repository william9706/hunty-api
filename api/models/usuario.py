from pydantic import BaseModel, EmailStr
from typing import Optional

# usuario model

class Usuario(BaseModel):
    UserId: str
    FirstName: str
    LastName: str
    Email:EmailStr
    YearsPreviousExperience: int
    Skills: list = []