import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.solicitud_model import TipoSolicitud
from fastapi.encoders import jsonable_encoder

class SolicitudController:
    def get_TipoSolicitud(self, TipoSolicitud_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tiposolicitud WHERE IDTipoSolicitud = %s", (TipoSolicitud_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'IDTipoSolicitud':int(result[0]),
                    'valor':result[1],
                    'descripcion':result[2]
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
    #TODAS LAS SOLICITUDES
    def get_TipoSolicitudes(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tiposolicitud")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'IDTipoSolicitud':data[0],
                    'valor':data[1],
                    'descripcion':data[2]
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