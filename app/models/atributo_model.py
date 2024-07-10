from pydantic import BaseModel

class Atributo(BaseModel):
    id: int
    nombre: str
    descripcion: str  