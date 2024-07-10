import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.area_model import Area
from fastapi.encoders import jsonable_encoder

class AreaController:
    def get_Area(self, Area_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM area WHERE IdArea = %s", (Area_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'IdArea':int(result[0]),
                    'Facultad':result[1],
                    'Programa':result[2]
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
    def get_Areas(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM area")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                        'IdArea': int(data[0]),
                        'Facultad':data[1],
                        'Programa':data[2]
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