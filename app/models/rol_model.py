from pydantic import BaseModel

class Rol(BaseModel):
    IdRol: int
    NombreRol: str
    DescripcionRol: str  
class Modulo(BaseModel):
    id: int
    modulo: str

class RoleModule(BaseModel):
    idrol: int
    idmodulo: int

class RoleCreate(BaseModel):
    nombre: str
    descripcion: str

class RoleDelete(BaseModel):
    id: int 