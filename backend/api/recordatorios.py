from fastapi import APIRouter, HTTPException
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

# Modelo de datos para los recordatorios
class Recordatorio(BaseModel):
    id: Optional[int]  # Asignado por el sistema
    titulo: str
    descripcion: str
    fecha_vencimiento: datetime
    completado: bool = False  # Por defecto, no completado

# Variable temporal para almacenar recordatorios (en lugar de una base de datos)
recordatorios_db = []
id_counter = 1  # Contador para asignar IDs únicos

# Ruta para obtener todos los recordatorios
@router.get("/recordatorios", response_model=List[Recordatorio])
async def obtener_recordatorios():
    return recordatorios_db

# Ruta para crear un nuevo recordatorio
@router.post("/recordatorios", response_model=Recordatorio)
async def crear_recordatorio(recordatorio: Recordatorio):
# Validar que el ID no sea parte de la solicitud entrante
    if recordatorio.id is not None:
        raise HTTPException(status_code=400, detail="ID should not be provided")
    
    # Crear el nuevo recordatorio con el ID generado automáticamente
    nuevo_recordatorio = recordatorio.model_copy(update={"id": id_counter})
    recordatorios_db.append(nuevo_recordatorio)
    id_counter += 1
    return nuevo_recordatorio

# Ruta para actualizar un recordatorio
@router.put("/recordatorios/{recordatorio_id}", response_model=Recordatorio)
async def actualizar_recordatorio(recordatorio_id: int, datos_actualizados: Recordatorio):
    for r in recordatorios_db:
        if r.id == recordatorio_id:
            r.titulo = datos_actualizados.titulo
            r.descripcion = datos_actualizados.descripcion
            r.fecha_vencimiento = datos_actualizados.fecha_vencimiento
            r.completado = datos_actualizados.completado
            return r
    raise HTTPException(status_code=404, detail="Recordatorio no encontrado")

# Ruta para eliminar un recordatorio
@router.delete("/recordatorios/{recordatorio_id}")
async def eliminar_recordatorio(recordatorio_id: int):
    global recordatorios_db
    recordatorios_db = [r for r in recordatorios_db if r.id != recordatorio_id]
    return {"message": "Recordatorio eliminado"}
