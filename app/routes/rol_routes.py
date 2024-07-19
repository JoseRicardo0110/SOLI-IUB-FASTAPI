from fastapi import APIRouter, HTTPException
from controllers.rol_controller import *
from models.rol_model import Rol
from typing import List
from fastapi.encoders import jsonable_encoder
import mysql.connector
from models.rol_model import Modulo
from models.rol_model import RoleModule
from models.rol_model import RoleCreate


router = APIRouter()

nuevo_rol = RolController()

@router.post("/create_rol")
def create_rol(role: RoleCreate):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Eliminar la restricción de clave foránea
        cursor.execute("ALTER TABLE rolxmodulo DROP FOREIGN KEY rolxmodulo_ibfk_1")

        # Modificar la columna IdRol para que sea autoincremental
        cursor.execute("ALTER TABLE rol MODIFY COLUMN IdRol INT NOT NULL AUTO_INCREMENT")

        # Insertar el nuevo rol
        cursor.execute("INSERT INTO rol (NombreRol, DescripcionRol) VALUES (%s, %s)", 
                       (role.nombre, role.descripcion))
        conn.commit()

        # Volver a añadir la restricción de clave foránea
        cursor.execute("ALTER TABLE rolxmodulo ADD CONSTRAINT rolxmodulo_ibfk_1 FOREIGN KEY (idrol) REFERENCES rol(IdRol) ON DELETE CASCADE ON UPDATE CASCADE")
        conn.commit()

        return {"message": "Role created successfully"}

    except mysql.connector.Error as err:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(err))
    finally:
        conn.close()

@router.post("/add_modulo_a_rol")
def add_modulo_a_rol(role_module: RoleModule):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO rolxmodulo (idrol, idmodulo) VALUES (%s, %s)", 
                       (role_module.idrol, role_module.idmodulo))
        conn.commit()
        return {"message": "Module added to role"}
                
    except mysql.connector.Error as err:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(err))
    finally:
        conn.close()

@router.delete("/remove_modulo_de_rol")
def remove_modulo_de_rol(role_module: RoleModule):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM rolxmodulo WHERE idrol = %s AND idmodulo = %s", 
                       (role_module.idrol, role_module.idmodulo))
        conn.commit()
        return {"message": "Module removed from role"}
                
    except mysql.connector.Error as err:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(err))
    finally:
        conn.close()
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
