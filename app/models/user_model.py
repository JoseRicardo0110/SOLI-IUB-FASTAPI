from pydantic import BaseModel


class User(BaseModel):
    IdArea: int
    usuario: str
    contrasena: str
    nombre: str
    apellido: str
    documento: str
    telefono: str
    correo: str
    
#  modelo para el login 
class userdb(BaseModel):
   
    usuario: str
    contrasena:str

   