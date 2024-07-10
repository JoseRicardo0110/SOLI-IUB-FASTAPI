from pydantic import BaseModel

class Rol(BaseModel):
    IdRol: int
    NombreRol: str
    DescripcionRol: str  