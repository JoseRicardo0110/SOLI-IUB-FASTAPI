import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.user_model import User
from models.user_model import userdb
from fastapi.encoders import jsonable_encoder
import time
import datetime
import jwt


SECRET_KEY="cleandeskpolicy123$"
ALGORITHM="HS256"
ACCES_TOKEN_EXPIRE_MIN="800"
class UserController:    
            
    def create_user(self, user: User):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            print("prueba1")
            cursor.execute("INSERT INTO usuario (IdArea,usuario,contrasena,nombre,apellido,documento,teléfono,correo) VALUES ( %s,%s, %s, %s, %s, %s, %s,%s)", (user.IdArea, user.usuario, user.contrasena, user.nombre, user.apellido, user.documento, user.telefono, user.correo))
            print("prueba2")
            conn.commit()
            conn.close()
            return {"resultado": "Usuario creado"}
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()


    def loginuser(self,loginvar:userdb):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT usuario.usuario, usuario.contrasena, usuario.id, usuario.nombre, rolxusuario.IdRol FROM usuario join rolxusuario on usuario.id = rolxusuario.IdXUsuario WHERE (usuario=%s and contrasena=%s) or correo=%s ",(loginvar.usuario,loginvar.contrasena,loginvar.usuario))
            result = cursor.fetchone()
            if result:
                # Definir el tiempo de expiración del token
                # Por ejemplo, 3600 segundos (1 hora)
                expires_in = datetime.timedelta(hours=1)
                expiration = datetime.datetime.utcnow() + expires_in
                content={
                    'usuario':str(result[0]),
                    'contrasena':str(result[1]),
                    'id':int(result[2]),
                    'nombre':str(result[3]),
                    'rol':int(result[4]),
                    'exp': expiration
                }
                encoded = jwt.encode(content,SECRET_KEY,algorithm="HS256")
                return {"access_token": encoded, "usuario":content}
            else:
                raise HTTPException(status_code=404, detail="usuario o contraseña son incorrectos")
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

          
    def verify_token(self, token: str):
        try:
            # Decodificar el token usando la clave secreta y el algoritmo
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            
            # Verificar si el token ha expirado
            exp = payload.get('exp', None)
            if exp is None or exp < time.time():
                raise jwt.ExpiredSignatureError("Token expirado")
            
            # Si todo está bien, devolver el payload del token
            return "Token valido"
        except jwt.PyJWTError as e:
            # Si hay un error al decodificar o verificar el token, lanzar una excepción HTTP
            raise HTTPException(status_code=401, detail="Token invalido")



    def delete_user(self, user_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM usuario WHERE id = %s", (user_id,))
            conn.commit()
            conn.close()
            return {"resultado": "Usuario eliminado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    def get_user(self, user_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario WHERE id = %s", (user_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'IdArea':int(result[1]),
                    'usuario':result[2],
                    'contrasena':result[3],
                    'nombre':result[4],
                    'apellido':result[5],
                    'documento':result[6],
                    'teléfono':result[7],
                    'correo':result[8]
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

    def get_solicitudcorreo(self, user_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT usua.* FROM solicitud sol join usuario usua on sol.idUsuario = usua.id WHERE sol.idSolicitud = %s", (user_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'IdArea':int(result[1]),
                    'usuario':result[2],
                    'contrasena':result[3],
                    'nombre':result[4],
                    'apellido':result[5],
                    'documento':result[6],
                    'teléfono':result[7],
                    'correo':result[8]
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

    def get_modulos(self, id_rol: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT idmodulo,detalle,modulo FROM rolxmodulo join modulos on rolxmodulo.idmodulo= modulos.id WHERE idrol = %s", (id_rol,))
            results = cursor.fetchall()
            payload = []
            i=1
            for data in results:
                content = {
                    'modulo':int(data[0]),
                    'detalle':data[1],
                    'modulos':data[2]

                }
                i=i+1
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)            
            return json_data          
        except mysql.connector.Error as err:
            conn.rollback()
            print(f"Database errorr: {err}") # Log the error for debugging
        finally:
            conn.close()
    def get_users(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT usuario.*, rol.NombreRol, rol.DescripcionRol FROM usuario JOIN rolxusuario ON usuario.id = rolxusuario.IdXUsuario JOIN rol ON rolxusuario.IdRol = rol.IdRol;")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'IdArea':data[1],
                    'usuario':data[2],
                    'contrasena':data[3],
                    'nombre':data[4],
                    'apellido':data[5],
                    'documento':data[6],
                    'teléfono':data[7],
                    'correo':data[8],
                    'nombrerol':data[9],
                    'descripcion':data[10]

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
    
    def update_user(self,user_id:int,user:User):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            print("prueba1")
            cursor.execute(("""
                UPDATE usuario
                SET IdArea = %s, usuario = %s, contrasena = %s,
                    nombre = %s, apellido = %s, documento = %s, teléfono = %s
                WHERE id = %s
                """),(
                    user.IdArea, user.usuario, user.contrasena, user.nombre, user.apellido, user.documento, user.teléfono, user_id
                ))
            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="usuario no encontrado")

            # Fetch updated data and return
            cursor.execute(f"SELECT * FROM usuario WHERE id='{user_id}'")
            result = cursor.fetchone()
            content = {
                    'id':int(result[0]),
                    'IdArea':int(result[1]),
                    'usuario':result[2],
                    'contrasena':result[3],
                    'nombre':result[4],
                    'apellido':result[5],
                    'documento':result[6],
                    'teléfono':result[7]
                }
            return content

        except Exception as err:
            # Handle other potential exceptions appropriately
            raise HTTPException(status_code=500, detail=f"Error al actualizar el usuario : {err}")

        finally:
            conn.close()            