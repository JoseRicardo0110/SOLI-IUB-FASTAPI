from pydantic import BaseModel

class Rol(BaseModel):
    IdRol: int
    NombreRol: str
    DescripcionRol: str  
class Modulo(BaseModel):
    id: int
    modulo: str
