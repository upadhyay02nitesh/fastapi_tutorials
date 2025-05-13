# schemas.py
from pydantic import BaseModel

class TeaCreate(BaseModel):
    name: str
    salary: float
