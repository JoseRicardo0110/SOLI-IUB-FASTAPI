from fastapi import APIRouter, HTTPException
from controllers.atributoxusuario_controller import *
from models.atributoxusuario_model import atributoxusuario

router = APIRouter()

nuevo_atributoxusuario = atributoxusuarioController()


@router.get("/get_atributoxusuario/{atributoxusuario_id}",response_model=atributoxusuario)
async def get_atributoxusuario(atributoxusuario_id: int):
    rpta = nuevo_atributoxusuario.get_atributoxusuario(atributoxusuario_id)
    return rpta

@router.get("/get_atributosxusuario/")
async def get_atributosxusuario():
    rpta =nuevo_atributoxusuario.get_atributosxusuario()
    return rpta