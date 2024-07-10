from pydantic import BaseModel

class Area(BaseModel):
    IdArea: int
    Facultad: str
    Programa: str  