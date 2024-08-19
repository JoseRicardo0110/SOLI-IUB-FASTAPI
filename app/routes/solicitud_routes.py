from openpyxl import Workbook
from fastapi import APIRouter, HTTPException, Query
from controllers.solicitud_controller import *
from models.solicitud_model import TipoSolicitud
from typing import Optional
from pydantic import BaseModel
from starlette.responses import FileResponse
import os
import datetime

router = APIRouter()

nuevo_solicitud = SolicitudController()

class ReportRequest(BaseModel):
    report_type: str
    start_date: str
    end_date: str
    area_id: Optional[int] = None

def convert_date_format(date_str: str) -> str:
    """Convert date from Y-m-d to d/m/Y to match database format."""
    return datetime.datetime.strptime(date_str, "%Y-%m-%d").strftime("%d/%m/%Y")

def execute_query(query: str, params: tuple):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, params)
    result = cursor.fetchall()
    conn.close()
    return result

@router.post("/report")
def get_report(request: ReportRequest):
    try:
        print("Request Data:", request)  # Debug print

        # Convertir las fechas al formato de la base de datos
        start_date = convert_date_format(request.start_date)
        end_date = convert_date_format(request.end_date)

        if request.report_type == "sin_asignar":
            query = """
                SELECT * FROM solicitud 
                WHERE idpersonaAsignada = 0 
                AND FechaCreacion BETWEEN %s AND %s
            """
            params = (start_date, end_date)
        elif request.report_type == "pendientes":
            query = """
                SELECT * FROM solicitud 
                WHERE estado = 'pendiente' 
                AND FechaCreacion BETWEEN %s AND %s
            """
            params = (start_date, end_date)
        elif request.report_type == "finalizadas":
            query = """
                SELECT * FROM solicitud 
                WHERE estado = 'finalizada' 
                AND FechaCreacion BETWEEN %s AND %s
            """
            params = (start_date, end_date)
        elif request.report_type == "pendientes_area" and request.area_id:
            query = """
                SELECT s.* 
                FROM solicitud s 
                JOIN usuario u ON s.idUsuario = u.id 
                WHERE s.estado = 'pendiente' 
                AND u.IdArea = %s 
                AND s.FechaCreacion BETWEEN %s AND %s
            """
            params = (request.area_id, start_date, end_date)
        elif request.report_type == "finalizadas_area" and request.area_id:
            query = """
                SELECT s.* 
                FROM solicitud s 
                JOIN usuario u ON s.idUsuario = u.id 
                WHERE s.estado = 'finalizada' 
                AND u.IdArea = %s 
                AND s.FechaCreacion BETWEEN %s AND %s
            """
            params = (request.area_id, start_date, end_date)
        else:
            query = """
                SELECT * FROM solicitud 
                WHERE FechaCreacion BETWEEN %s AND %s
            """
            params = (start_date, end_date)

        print("Executing Query:", query)  # Debug print
        print("With Parameters:", params)  # Debug print

        result = execute_query(query, params)

        print("Query Result:", result)  # Debug print
        
        if not result:
            raise HTTPException(status_code=404, detail="No se encontraron datos para los parámetros especificados")

        # Crear el archivo Excel
        wb = Workbook()
        ws = wb.active
        ws.title = "Report"

        # Escribir los encabezados
        headers = list(result[0].keys())
        ws.append(headers)

        # Escribir los datos
        for row in result:
            ws.append(list(row.values()))

        # Guardar el archivo
        file_path = "/tmp/report.xlsx"
        wb.save(file_path)
        
        if not os.path.exists(file_path):
            raise HTTPException(status_code=500, detail="El archivo Excel no se generó correctamente.")

        print("Excel file created at:", file_path)  # Debug print

        return FileResponse(file_path, filename="report.xlsx")

    except mysql.connector.Error as err:
        print("MySQL Error:", err)  # Debug print
        raise HTTPException(status_code=500, detail=str(err))
    except Exception as e:
        print("Error:", e)  # Debug print
        raise HTTPException(status_code=500, detail=str(e))
