from fastapi import FastAPI
from backend.api import recordatorios

# Inicialización de la aplicación
app = FastAPI()

# Incluir los routers
app.include_router(recordatorios.router, prefix="/api")

# Endpoints simples
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/health")
def health_check():
    return {"status": "Healthy"}
