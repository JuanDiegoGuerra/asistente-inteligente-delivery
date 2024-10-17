from fastapi import APIRouter
from typing import List
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

# Modelo de datos para los recordatorios
class Recordatorio(BaseModel):
    id: int
    titulo: str
    descripcion: str
    fecha: datetime
    completado: bool = False

# Variable temporal para almacenar recordatorios (en lugar de una base de datos)
recordatorios_db = []