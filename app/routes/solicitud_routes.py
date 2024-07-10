from fastapi import APIRouter, HTTPException
from controllers.solicitud_controller import *
from models.solicitud_model import TipoSolicitud

router = APIRouter()

nuevo_solicitud = SolicitudController()

"""@router.post("/create_user/")
async def create_user(user: User):
    rpta = nuevo_solicitud.create_user(user)
    return rpta"""

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
