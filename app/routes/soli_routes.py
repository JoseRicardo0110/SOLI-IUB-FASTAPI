from fastapi import APIRouter, HTTPException
from controllers.soli_controller import *


router = APIRouter()

nuevo_soli = solicitudController()

@router.post("/create_Solicitud/")
async def create_Solicitud(solicitud: Creasoli):
    rpta = nuevo_soli.create_Solicitud(solicitud)
    return rpta

@router.post("/asignarme")
async def asignarme(solicitud: actualizasoli):
    rpta = nuevo_soli.asignarme(solicitud)
    return rpta

@router.post("/responder")
async def responder(informacion: respuesta):
    rpta = nuevo_soli.responder(informacion)
    return rpta

@router.post("/finalizar_solicitud")
async def finalizar_solicitud(info: Estado):
    rpta = nuevo_soli.finalizar_solicitud(info)
    return rpta

@router.get("/get_SolicitudesPendientesPorIdPersonaAsignada/{idpersonaAsignada}")
async def get_SolicitudesPendientesPorIdPersonaAsignada(idpersonaAsignada:int):
    rpta=nuevo_soli.get_SolicitudesPendientesPorIdPersonaAsignada(idpersonaAsignada)
    return rpta

@router.get("/get_SolicitudesFinalizadasPorIdPersonaAsignada/{idpersonaAsignada}")
async def get_SolicitudesFinalizadasPorIdPersonaAsignada(idpersonaAsignada:int):
    rpta=nuevo_soli.get_SolicitudesFinalizadasPorIdPersonaAsignada(idpersonaAsignada)
    return rpta

@router.get("/get_SolicitudesPendientesPorIdUsuario/{idUsuario}")
async def get_SolicitudesPendientesPorIdUsuario(idUsuario:int):
    rpta =nuevo_soli.get_SolicitudesPendientesPorIdUsuario(idUsuario)
    return rpta

@router.get("/get_SolicitudesFinalizadas/")
async def get_SolicitudesFinalizadas():
    rpta = nuevo_soli.get_SolicitudesFinalizadas()
    return rpta

@router.get("/get_Solicitudes/")
async def get_Solicitudes():
    rpta = nuevo_soli.get_Solicitudes()
    return rpta

@router.get("/get_SolicitudesFinalizadasPorIdUsuario/{idUsuario}")
async def get_SolicitudesFinalizadasPorIdUsuario(idUsuario:int):
    rpta = nuevo_soli.get_SolicitudesFinalizadasPorIdUsuario(idUsuario)
    return rpta

@router.get("/get_SolicitudesSinAsignar/")
async def get_SolicitudesSinAsignar():
    rpta = nuevo_soli.get_SolicitudesSinAsignar()
    return rpta

@router.get("/get_SolicitudesPendientes/")
async def get_SolicitudesPendientes():
    rpta = nuevo_soli.get_SolicitudesPendientes()
    return rpta

@router.get("/get_Solicitud/{Solicitud_id}")
async def get_Solicitud(Solicitud_id: int):
    rpta = nuevo_soli.get_Solicitud(Solicitud_id)
    return rpta


@router.get("/get_soli/{id_soli}")
async def get_soli(id_soli: int):
    rpta = nuevo_soli.get_soli(id_soli)
    return rpta

