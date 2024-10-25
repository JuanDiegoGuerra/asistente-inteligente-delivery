from fastapi import APIRouter, HTTPException
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime, timezone, timedelta

router = APIRouter()

# Modelo de datos para los recordatorios
class Recordatorio(BaseModel):
    id: Optional[int] = None  # Asignado por el sistema, inicializado en None
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
    global id_counter
    # Validar que el ID no sea parte de la solicitud entrante
    if recordatorio.id is not None:
        raise HTTPException(status_code=400, detail="ID should not be provided")
    
    # Asignar un nuevo ID y agregar el recordatorio a la base de datos
    nuevo_recordatorio = recordatorio.copy(update={"id": id_counter})
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

@router.get("/recordatorios/proximos", response_model=List[Recordatorio])
async def obtener_recordatorios_proximos():
    ahora = datetime.now(timezone.utc)  # Obtener la fecha actual en UTC con zona horaria "aware"
    print(f"Fecha actual con zona horaria: {ahora}")

    proximos_recordatorios = [
        r for r in recordatorios_db
        # Convertimos la fecha de vencimiento a "aware" si es "naive", para evitar errores de comparación
        if r.fecha_vencimiento.replace(tzinfo=timezone.utc) <= (ahora + timedelta(hours=24)) and not r.completado
    ]
    print(f"Recordatorios próximos: {proximos_recordatorios}")
    return proximos_recordatorios