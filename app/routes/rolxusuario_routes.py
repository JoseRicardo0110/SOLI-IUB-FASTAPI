from fastapi import APIRouter, HTTPException
from controllers.rolxusuario_controller import *
from models.rolxusuario_model import rolxusuario

router = APIRouter()

nuevo_rolxusuario = rolxusuariocontroller()

@router.get("/get_rolesxusuario/")
async def get_rolesxusuario():
    rpta = nuevo_rolxusuario.get_rolesxusuario()
    return rpta

@router.get("/get_rolxusuario/{rolxusuario_id}")
async def get_rolxusuario(rolxusuario_id: int):
    rpta = nuevo_rolxusuario.get_rolxusuario(rolxusuario_id)
    return rpta