from fastapi import APIRouter, HTTPException
from controllers.user_controller import *
from models.user_model import User


router = APIRouter()

nuevo_usuario = UserController()

""" ruta para ingresar por el login con jwt """
@router.post("/loginuser")
async def loginuser(loginvar: userdb):
    rpta = nuevo_usuario.loginuser(loginvar)
    return rpta

""" ruta para crear un nuevo usuario """
@router.post("/create_user/")
async def create_user(user: User):
    rpta = nuevo_usuario.create_user(user)
    return rpta

@router.put("/update_user/{user_id}")
async def update_user(user_id: int, data: User):
    rpta = nuevo_usuario.update_user(user_id,data)
    return rpta

@router.delete("/delete_user/{user_id}")
async def delete_user(user_id: int):
    rpta = nuevo_usuario.delete_user(user_id)
    return rpta

@router.get("/get_user/{user_id}",response_model=User)
async def get_user(user_id: int):
    rpta = nuevo_usuario.get_user(user_id)
    return rpta

@router.get("/get_solicitudcorreo/{id_soli}",response_model=User)
async def get_solicitudcorreo(id_soli: int):
    rpta = nuevo_usuario.get_solicitudcorreo(id_soli)
    return rpta

@router.get("/get_modulos/{id_rol}")
async def get_modulos(id_rol: int):
    rpta = nuevo_usuario.get_modulos(id_rol)
    return rpta

@router.get("/get_users/")
async def get_users():
    rpta = nuevo_usuario.get_users()
    return rpta

