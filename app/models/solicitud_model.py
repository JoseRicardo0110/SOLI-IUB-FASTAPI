from pydantic import BaseModel

class TipoSolicitud(BaseModel):
    IDTipoSolicitud: int
    valor: str
    descripcion: str  
    
    
        