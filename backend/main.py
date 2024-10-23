from fastapi import FastAPI
from backend.api import recordatorios, promociones
from fastapi.middleware.cors import CORSMiddleware

# Inicialización de la aplicación
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000/"],  # Cambia "*" por la URL de tu frontend en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
