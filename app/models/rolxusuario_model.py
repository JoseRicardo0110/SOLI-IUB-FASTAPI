from pydantic import BaseModel

class rolxusuario(BaseModel):
    Id:int
    IdXUsuario:int
    IdRol:int
    ValorRolXUsuario:str
    DescripcionRolXUsuario:str