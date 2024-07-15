from fastapi import APIRouter, HTTPException
from controllers.rol_controller import *
from models.rol_model import Rol
from typing import List
from fastapi.encoders import jsonable_encoder
import mysql.connector


router = APIRouter()

nuevo_rol = RolController()

@router.get("/get_all_modulos", response_model=List[dict])
def get_all_modulos():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, modulo FROM modulos")
        result = cursor.fetchall()
        payload = []

        for mod in result:
            content = {
                'id': mod[0],
                'modulo': mod[1]
            }
            payload.append(content)

        json_data = jsonable_encoder(payload)            
        if result:
            return json_data
        else:
            raise HTTPException(status_code=404, detail="No modules found")  
                
    except mysql.connector.Error as err:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(err))
    finally:
        conn.close()

@router.get("/get_Roles/")
async def get_Roles():
    rpta = nuevo_rol.get_Roles()
    return rpta
"""@router.get("/get_all_modulos")
async def get_all_modulos():
    rpta = nuevo_rol.get_all_modulos()
    return rpta"""
@router.get("/get_ModulosxRoles")
async def get_ModulosxRoles():
    rpta = nuevo_rol.get_ModulosxRoles()
    return rpta

@router.get("/get_Rol/{Rol_id}",response_model=Rol)
async def get_Rol(Rol_id: int):
    rpta = nuevo_rol.get_Rol(Rol_id)
    return rpta
