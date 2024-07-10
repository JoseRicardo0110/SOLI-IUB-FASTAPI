from pydantic import BaseModel

class atributoxusuario(BaseModel):
    id: int
    idusuario:int
    idatributo:int  
    valor:str
    descripcion:str