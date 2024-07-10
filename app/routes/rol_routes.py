from fastapi import APIRouter, HTTPException
from controllers.rol_controller import *
from models.rol_model import Rol

router = APIRouter()

nuevo_rol = RolController()

@router.get("/get_Roles/")
async def get_Roles():
    rpta = nuevo_rol.get_Roles()
    return rpta
@router.get("/get_ModulosxRoles")
async def get_ModulosxRoles():
    rpta = nuevo_rol.get_ModulosxRoles()
    return rpta

@router.get("/get_Rol/{Rol_id}",response_model=Rol)
async def get_Rol(Rol_id: int):
    rpta = nuevo_rol.get_Rol(Rol_id)
    return rpta
