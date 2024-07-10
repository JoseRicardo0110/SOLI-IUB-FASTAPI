from fastapi import APIRouter, HTTPException
from controllers.atributo_controller import *
from models.atributo_model import Atributo

router = APIRouter()

nuevo_atributo = AtributoController()


@router.get("/get_Atributo/{Atributo_id}",response_model=Atributo)
async def get_Atributo(Atributo_id: int):
    rpta = nuevo_atributo.get_Atributo(Atributo_id)
    return rpta

@router.get("/get_Atributos/")
async def get_Atributos():
    rpta = nuevo_atributo.get_Atributos()
    return rpta