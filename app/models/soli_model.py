from pydantic import BaseModel

class Solicitud(BaseModel):
    idSolicitud:int
    idUsuario:int
    IdTipoSolicitud:int
    idpersonaAsignada:int
    Archivos:str
    Asunto:str
    nota:str
    FechaCreacion:str
    FechaUltimaModificacion:str
    estado:str
    prioridad:str

class Creasoli(BaseModel):
    idUsuario : int
    IdTipoSolicitud : int
    Asunto : str
    FechaCreacion: str

class actualizasoli(BaseModel):
    idUsuario : int
    id : int
    nombre: str
    FechaUltimaModificacion: str
    correo: str

class respuesta(BaseModel):
    id : int
    texto: str
    correo: str
    FechaUltimaModificacion: str
    
class Estado(BaseModel):
    id : int
    fecha: str
    correo: str