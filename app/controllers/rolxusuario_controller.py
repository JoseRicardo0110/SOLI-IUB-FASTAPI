import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.rolxusuario_model import rolxusuario
from fastapi.encoders import jsonable_encoder

class rolxusuariocontroller:
    def get_rolxusuario(self,rolxusuario_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM rolxusuario WHERE IdXUsuario = %s", (rolxusuario_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            content={
                    'Id':int(result[0]),
                    'IdXUsuario':int(result[1]),
                    'IdRol':int(result[2]),
                    'ValorRolXUsuario':result[3],
                    'DescripcionRolXUsuario':result[4]
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
    def get_rolesxusuario(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM rolxusuario")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'Id': data[0],
                    'IdXUsuario':data[1],
                    'IdRol':data[2],
                    'ValorRolXUsuario':data[3],
                    'DescripcionRolXUsuario':data[4],
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