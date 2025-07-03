from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from DB.conexion import motor
from models.base import Base
from RestController.RestCrudPacientes import router as pacientes_router
from RestController.Cuestionario import router as formularios_router
from fastapi.responses import JSONResponse
import uvicorn

# Crear la aplicación FastAPI
app = FastAPI(
    title="API de Gestión de Pacientes",
    description="API para la gestión de pacientes y sus formularios",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar los orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint raíz
@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de Gestión de Pacientes", "docs": "/docs"}

# Incluir routers con prefijo base /api/v1
app.include_router(pacientes_router, prefix="/api/v1")
app.include_router(formularios_router, prefix="/api/v1")

# Evento de inicio de la aplicación
@app.on_event("startup")
async def iniciar_aplicacion():
    # Crear tablas si no existen
    Base.metadata.create_all(bind=motor)
    print("Base de datos inicializada correctamente")

# Punto de entrada de la aplicación
if __name__ == "__main__":
    uvicorn.run(
        "Main:app",
        host="0.0.0.0",
        port=5500,
        reload=True,
        log_level="info"
    )
