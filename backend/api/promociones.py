from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from transformers import pipeline
import os
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()

router = APIRouter()

# Inicializa el pipeline de generación de texto con GPT-2
generator = pipeline('text-generation', model='gpt2')

# Modelo de datos para la petición
class PromocionRequest(BaseModel):
    tipo_comida: str
    horario: str  # Puede ser: "desayuno", "almuerzo", "cena"

@router.post("/generar-promocion")
async def generar_promocion(promocion: PromocionRequest):
    prompt = f"Write a message that says you want a {promocion.tipo_comida} for {promocion.horario}."

    try:
        # Generación de texto con el modelo GPT-2
        response = generator(prompt, max_length=60, num_return_sequences=1)
        mensaje_generado = response[0]['generated_text'].strip()
        return {"mensaje_promocional": mensaje_generado}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
