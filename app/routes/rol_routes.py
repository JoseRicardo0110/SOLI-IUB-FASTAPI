from fastapi import APIRouter, HTTPException
from controllers.rol_controller import *
from models.rol_model import Rol
from typing import List
from fastapi.encoders import jsonable_encoder
import mysql.connector
from models.rol_model import Modulo
from models.rol_model import RoleModule
from models.rol_model import RoleCreate
from models.rol_model import RoleDelete


router = APIRouter()

nuevo_rol = RolController()

@router.delete("/delete_rol")
def delete_rol(role: RoleDelete):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Obtener y eliminar las restricciones de claves foráneas en rolxmodulo
        cursor.execute("SHOW CREATE TABLE rolxmodulo")
        result_rolxmodulo = cursor.fetchone()
        create_table_sql_rolxmodulo = result_rolxmodulo[1]
        foreign_key_name_rolxmodulo = None

        for line in create_table_sql_rolxmodulo.split('\n'):
            if 'FOREIGN KEY' in line and 'REFERENCES `rol`' in line:
                foreign_key_name_rolxmodulo = line.split('CONSTRAINT `')[1].split('`')[0]
                break

        if foreign_key_name_rolxmodulo:
            cursor.execute(f"ALTER TABLE rolxmodulo DROP FOREIGN KEY {foreign_key_name_rolxmodulo}")

        # Obtener y eliminar las restricciones de claves foráneas en rolxusuario
        cursor.execute("SHOW CREATE TABLE rolxusuario")
        result_rolxusuario = cursor.fetchone()
        create_table_sql_rolxusuario = result_rolxusuario[1]
        foreign_key_name_rolxusuario = None

        for line in create_table_sql_rolxusuario.split('\n'):
            if 'FOREIGN KEY' in line and 'REFERENCES `rol`' in line:
                foreign_key_name_rolxusuario = line.split('CONSTRAINT `')[1].split('`')[0]
                break

        if foreign_key_name_rolxusuario:
            cursor.execute(f"ALTER TABLE rolxusuario DROP FOREIGN KEY {foreign_key_name_rolxusuario}")

        # Eliminar el rol
        cursor.execute("DELETE FROM rol WHERE IdRol = %s", (role.id,))
        conn.commit()

        # Volver a añadir las restricciones de claves foráneas
        if foreign_key_name_rolxmodulo:
            cursor.execute(f"ALTER TABLE rolxmodulo ADD CONSTRAINT {foreign_key_name_rolxmodulo} FOREIGN KEY (idrol) REFERENCES rol(IdRol) ON DELETE CASCADE ON UPDATE CASCADE")

        if foreign_key_name_rolxusuario:
            cursor.execute(f"ALTER TABLE rolxusuario ADD CONSTRAINT {foreign_key_name_rolxusuario} FOREIGN KEY (IdRol) REFERENCES rol(IdRol) ON DELETE CASCADE ON UPDATE CASCADE")

        conn.commit()

        return {"message": "Role deleted successfully"}

    except mysql.connector.Error as err:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(err))
    finally:
        conn.close()

@router.post("/create_rol")
def create_rol(role: RoleCreate):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Verificar y eliminar las restricciones de claves foráneas
        cursor.execute("SHOW CREATE TABLE rolxmodulo")
        result_rolxmodulo = cursor.fetchone()
        create_table_sql_rolxmodulo = result_rolxmodulo[1]
        foreign_key_name_rolxmodulo = None

        for line in create_table_sql_rolxmodulo.split('\n'):
            if 'FOREIGN KEY' in line and 'REFERENCES `rol`' in line:
                foreign_key_name_rolxmodulo = line.split('CONSTRAINT `')[1].split('`')[0]
                break

        if foreign_key_name_rolxmodulo:
            cursor.execute(f"ALTER TABLE rolxmodulo DROP FOREIGN KEY {foreign_key_name_rolxmodulo}")

        cursor.execute("SHOW CREATE TABLE rolxusuario")
        result_rolxusuario = cursor.fetchone()
        create_table_sql_rolxusuario = result_rolxusuario[1]
        foreign_key_name_rolxusuario = None

        for line in create_table_sql_rolxusuario.split('\n'):
            if 'FOREIGN KEY' in line and 'REFERENCES `rol`' in line:
                foreign_key_name_rolxusuario = line.split('CONSTRAINT `')[1].split('`')[0]
                break

        if foreign_key_name_rolxusuario:
            cursor.execute(f"ALTER TABLE rolxusuario DROP FOREIGN KEY {foreign_key_name_rolxusuario}")

        # Modificar la columna IdRol para que sea autoincremental
        cursor.execute("ALTER TABLE rol MODIFY COLUMN IdRol INT NOT NULL AUTO_INCREMENT")

        # Insertar el nuevo rol
        cursor.execute("INSERT INTO rol (NombreRol, DescripcionRol) VALUES (%s, %s)", 
                       (role.nombre, role.descripcion))
        conn.commit()

        # Volver a añadir las restricciones de claves foráneas
        if foreign_key_name_rolxmodulo:
            cursor.execute(f"ALTER TABLE rolxmodulo ADD CONSTRAINT {foreign_key_name_rolxmodulo} FOREIGN KEY (idrol) REFERENCES rol(IdRol) ON DELETE CASCADE ON UPDATE CASCADE")

        if foreign_key_name_rolxusuario:
            cursor.execute(f"ALTER TABLE rolxusuario ADD CONSTRAINT {foreign_key_name_rolxusuario} FOREIGN KEY (IdRol) REFERENCES rol(IdRol) ON DELETE CASCADE ON UPDATE CASCADE")

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
