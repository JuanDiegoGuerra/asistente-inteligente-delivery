from fastapi import APIRouter
from pydantic import BaseModel
import openai

router = APIRouter()

# Modelo de datos para la petición
class PromocionRequest(BaseModel):
    tipo_comida: str
    horario: str  # Puede ser: "mañana", "tarde", "noche"

# API key de OpenAI
openai.api_key = "TU_API_KEY"

@router.post("/generar-promocion")
async def generar_promocion(promocion: PromocionRequest):
    # Mensaje base para generar la promoción
    prompt = f"Genera un mensaje promocional para {promocion.tipo_comida} en el horario de {promocion.horario}."

    try:
        # Llamada a la API de OpenAI usando ChatCompletion
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente que genera mensajes promocionales para una empresa de delivery de comida."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=60
        )
        mensaje_generado = response['choices'][0]['message']['content'].strip()
        return {"mensaje_promocional": mensaje_generado}

    except Exception as e:
        return {"error": str(e)}
