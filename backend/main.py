import os
import openai
from dotenv import load_dotenv
from fastapi import FastAPI
from backend.api import recordatorios, promociones

# Cargar las variables de entorno
load_dotenv()

# Obtener la API Key
api_key = os.getenv("OPENAI_API_KEY")
print(f"API Key: {api_key}")  # Imprime la API Key para verificar

# Configurar OpenAI
openai.api_key = api_key

# Inicialización de la aplicación
app = FastAPI()

# Incluir los routers
app.include_router(recordatorios.router, prefix="/api")
app.include_router(promociones.router, prefix="/api")

# Endpoints simples
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/health")
def health_check():
    return {"status": "Healthy"}