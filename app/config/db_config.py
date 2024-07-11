import mysql.connector
""" from dotenv import load_dotenv
import os """

""" load_dotenv() """
Host = 'bj46jv7kpkrxwtgl7d7r-mysql.services.clever-cloud.com'
User = 'ujas9020kpamfmdk'
Password = 'XN4YSWP1qBoVNuRmMam1'
Database = 'bj46jv7kpkrxwtgl7d7r'
""" Host = os.getenv('MYSQ_HOST', '')
User = os.getenv('MYSQ_USER', 'root')
Password = os.getenv('MYSQ_PASSWORD', "")
Database = os.getenv('MYSQ_DB', "") """

# ? Conneccion a la base de datos en la nube clever-cloud
def get_db_connection():
    return mysql.connector.connect(
        host=Host,
        user=User,
        password=Password,
        database=Database)