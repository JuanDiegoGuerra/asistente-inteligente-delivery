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
