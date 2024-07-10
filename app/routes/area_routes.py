from fastapi import APIRouter, HTTPException
from controllers.area_controller import *
from models.area_model import Area

router = APIRouter()

nuevo_area = AreaController()

@router.get("/get_Areas/")
async def get_Areas():
    rpta = nuevo_area.get_Areas()
    return rpta

@router.get("/get_Area/{Area_id}",response_model=Area)
async def get_Area(Area_id: int):
    rpta = nuevo_area.get_Area(Area_id)
    return rpta

