from fastapi import APIRouter, HTTPException, Query
from controllers.solicitud_controller import *
from models.solicitud_model import TipoSolicitud
from typing import Optional
from pydantic import BaseModel
from starlette.responses import FileResponse
import pandas as pd

router = APIRouter()

nuevo_solicitud = SolicitudController()

"""@router.post("/create_user/")
async def create_user(user: User):
    rpta = nuevo_solicitud.create_user(user)
    return rpta"""
def execute_query(query: str, params: tuple):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, params)
    result = cursor.fetchall()
    conn.close()
    return result

class ReportRequest(BaseModel):
    report_type: str
    start_date: str
    end_date: str
    area_id: Optional[int] = None

@router.post("/report")
def get_report(request: ReportRequest):
    try:
        if request.report_type == "sin_asignar":
            query = "SELECT * FROM solicitud WHERE idpersonaAsignada = 0 AND FechaCreacion BETWEEN %s AND %s"
            params = (request.start_date, request.end_date)
        elif request.report_type == "pendientes":
            query = "SELECT * FROM solicitud WHERE estado = 'pendiente' AND FechaCreacion BETWEEN %s AND %s"
            params = (request.start_date, request.end_date)
        elif request.report_type == "finalizadas":
            query = "SELECT * FROM solicitud WHERE estado = 'finalizada' AND FechaCreacion BETWEEN %s AND %s"
            params = (request.start_date, request.end_date)
        elif request.report_type == "pendientes_area" and request.area_id:
            query = "SELECT s.* FROM solicitud s JOIN usuario u ON s.idUsuario = u.id JOIN area a ON u.IdArea = a.IdArea WHERE s.estado = 'pendiente' AND a.IdArea = %s AND s.FechaCreacion BETWEEN %s AND %s"
            params = (request.area_id, request.start_date, request.end_date)
        elif request.report_type == "finalizadas_area" and request.area_id:
            query = "SELECT s.* FROM solicitud s JOIN usuario u ON s.idUsuario = u.id JOIN area a ON u.IdArea = a.IdArea WHERE s.estado = 'finalizada' AND a.IdArea = %s AND s.FechaCreacion BETWEEN %s AND %s"
            params = (request.area_id, request.start_date, request.end_date)
        else:
            query = "SELECT * FROM solicitud WHERE FechaCreacion BETWEEN %s AND %s"
            params = (request.start_date, request.end_date)

        result = execute_query(query, params)
        
        # Convert result to DataFrame and save as Excel
        df = pd.DataFrame(result)
        file_path = "/tmp/report.xlsx"
        df.to_excel(file_path, index=False)
        
        return FileResponse(file_path, filename="report.xlsx")

    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=str(err))


@router.put("/update_TipoSolicitud/{TipoSolicitud_id}")
async def update_TipoSolicitud(TipoSolicitud_id: int, data: TipoSolicitud):
    rpta = nuevo_solicitud.update_TipoSolicitud(TipoSolicitud_id,data)
    return rpta

@router.delete("/delete_TipoSolicitud/{TipoSolicitud_id}")
async def delete_TipoSolicitud(TipoSolicitud_id: int):
    rpta = nuevo_solicitud.delete_TipoSolicitud(TipoSolicitud_id)
    return rpta

@router.get("/get_TipoSolicitudes/")
async def get_TipoSolicitudes():
    rpta = nuevo_solicitud.get_TipoSolicitudes()
    return rpta

@router.get("/get_TipoSolicitud/{TipoSolicitud_id}",response_model=TipoSolicitud)
async def get_TipoSolicitud(TipoSolicitud_id: int):
    rpta = nuevo_solicitud.get_TipoSolicitud(TipoSolicitud_id)
    return rpta
