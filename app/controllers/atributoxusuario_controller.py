import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.atributoxusuario_model import atributoxusuario
from fastapi.encoders import jsonable_encoder

class atributoxusuarioController:
    def get_atributoxusuario(self, atributoxusuario_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM atributoxusuario WHERE id = %s", (atributoxusuario_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'idusuario':int(result[1]),
                    'idatributo':int(result[2]),
                    'valor':result[3],
                    'descripcion':result[4],
                    
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


    def get_atributosxusuario(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM atributoxusuario")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                   'id':data[0],
                   'idusuario':data[1],
                   'idatributo':data[2],
                   'valor':data[3],
                   'descripcion':data[4],
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="atributos no encontrados")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()