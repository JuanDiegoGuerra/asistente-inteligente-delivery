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

# Ruta para obtener todos los recordatorios
@router.get("/recordatorios", response_model=List[Recordatorio])
async def obtener_recordatorios():
    return recordatorios_db

# Ruta para crear un nuevo recordatorio
@router.post("/recordatorios", response_model=Recordatorio)
async def crear_recordatorio(recordatorio: Recordatorio):
    recordatorios_db.append(recordatorio)
    return recordatorio

# Ruta para actualizar un recordatorio
@router.put("/recordatorios/{recordatorio_id}", response_model=Recordatorio)
async def actualizar_recordatorio(recordatorio_id: int, datos_actualizados: Recordatorio):
    for r in recordatorios_db:
        if r.id == recordatorio_id:
            r.titulo = datos_actualizados.titulo
            r.descripcion = datos_actualizados.descripcion
            r.fecha = datos_actualizados.fecha
            r.completado = datos_actualizados.completado
            return r
    return {"error": "Recordatorio no encontrado"}

# Ruta para eliminar un recordatorio
@router.delete("/recordatorios/{recordatorio_id}")
async def eliminar_recordatorio(recordatorio_id: int):
    global recordatorios_db
    recordatorios_db = [r for r in recordatorios_db if r.id != recordatorio_id]
    return {"message": "Recordatorio eliminado"}