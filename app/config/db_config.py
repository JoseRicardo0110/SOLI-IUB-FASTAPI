import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
Host = os.getenv('MYSQ_HOST', 'localhost')
User = os.getenv('MYSQ_USER', 'root')
Password = os.getenv('MYSQ_PASSWORD', "")
Database = os.getenv('MYSQ_DB', "bdjosemaria")

# ? Conneccion a la base de datos en la nube clever-cloud
def get_db_connection():
    return mysql.connector.connect(
        host=Host,
        user=User,
        password=Password,
        database=Database)