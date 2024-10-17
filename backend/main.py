from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Ruta para verificar que la aplicación está corriendo correctamente
@app.get("/health")
def health_check():
    return {"status": "Healthy"}
