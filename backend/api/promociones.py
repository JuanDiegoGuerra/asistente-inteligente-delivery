from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from transformers import pipeline

router = APIRouter()

# Cargar modelo preentrenado de Hugging Face
generator = pipeline('text-generation', model='gpt2')

# Modelo de datos para la petición
class PromocionRequest(BaseModel):
    tipo_comida: str
    horario: str  # Puede ser: "mañana", "tarde", "noche"

@router.post("/generar-promocion")
async def generar_promocion(promocion: PromocionRequest):
    prompt = f"Genera un mensaje promocional para {promocion.tipo_comida} en el horario de {promocion.horario}."

    try:
        # Generar texto usando Hugging Face GPT-2
        response = generator(prompt, max_length=60, num_return_sequences=1)
        mensaje_generado = response[0]['generated_text'].strip()
        return {"mensaje_promocional": mensaje_generado}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
