from fastapi import APIRouter, HTTPException
from controllers.user_controller import *
from models.user_model import User
from models.user_model import UserCreate


router = APIRouter()

nuevo_usuario = UserController()

@router.post("/create_user")
def create_user(user: UserCreate):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Insertar el nuevo usuario
        cursor.execute("""
            INSERT INTO usuario (IdArea, usuario, contrasena, nombre, apellido, documento, telefono, correo) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (user.IdArea, user.usuario, user.contrasena, user.nombre, user.apellido, user.documento, user.telefono, user.correo))
        user_id = cursor.lastrowid

        # Asignar rol al nuevo usuario
        cursor.execute("""
            INSERT INTO rolxusuario (IdXUsuario, IdRol) 
            VALUES (%s, %s)
        """, (user_id, user.rol))

        conn.commit()

        return {"message": "User created successfully"}
    except mysql.connector.Error as err:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(err))
    finally:
        conn.close()

""" ruta para ingresar por el login con jwt """
@router.post("/loginuser")
async def loginuser(loginvar: userdb):
    rpta = nuevo_usuario.loginuser(loginvar)
    return rpta

""" ruta para crear un nuevo usuario """
@router.post("/create_use/")
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

