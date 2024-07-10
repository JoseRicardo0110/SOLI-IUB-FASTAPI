import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.rol_model import Rol
from fastapi.encoders import jsonable_encoder

class RolController:
    def get_Rol(self, Area_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM rol WHERE IdRol = %s", (Area_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'IdRol':int(result[0]),
                    'NombreRol':result[1],
                    'DescripcionRol':result[2]
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="User not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
            
        #TODAS LAS AREAS
    def get_ModulosxRoles(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT NombreRol,DescripcionRol,modulo FROM rol join rolxmodulo on rol.IdRol= rolxmodulo.idrol join modulos on rolxmodulo.idmodulo= modulos.id ")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'NombreRol':data[0],
                    'DescripcionRol':data[1],
                    'modulo':data[2]
                    
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="User not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    def get_Roles(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM rol")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'IdRol':data[0],
                    'NombreRol':data[1],
                    'DescripcionRol':data[2]
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="User not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()