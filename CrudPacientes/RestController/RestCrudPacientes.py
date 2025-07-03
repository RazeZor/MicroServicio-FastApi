from fastapi import APIRouter, Depends, Request, HTTPException, status
from sqlalchemy.orm import Session
from DB.conexion import MINUTOS_EXPIRACION_TOKEN, CLAVE_SECRETA
from DB.dependencias import obtener_sesion, verificar_token
from models.modelos import Paciente
from datetime import datetime, timedelta
from typing import Dict, Any
from pydantic import BaseModel
import jwt

# Crear el enrutador con prefijo
router = APIRouter(prefix="/pacientes", tags=["pacientes"])

# Modelo para el token
class Token(BaseModel):
    access_token: str
    token_type: str

# Función para crear token # si me fijo bien Dict es un disccionario que va a devolver 2 
# valores de tipo String 
def crear_token() -> Dict[str, str]: #
    expiracion = datetime.utcnow() + timedelta(minutes=MINUTOS_EXPIRACION_TOKEN)
    datos_a_codificar = {"exp": expiracion}
    token_jwt = jwt.encode(datos_a_codificar, CLAVE_SECRETA, algorithm="HS256")
    return {"access_token": token_jwt, "token_type": "bearer"}

# Endpoint para obtener token
@router.get("/token")
def obtener_token() -> Dict[str, str]:
    return crear_token()

# Endpoint de prueba
@router.get("/")
def index() -> Dict[str, str]:
    return {"mensaje": "API de Pacientes"}

# Endpoint para agregar paciente
@router.post("/AgregarPaciente")
async def agregar_paciente(
    solicitud: Request, 
    sesion: Session = Depends(obtener_sesion), 
    datos_token: Dict[str, Any] = Depends(verificar_token)
) -> Dict[str, str]:
    try:
        datos = await solicitud.json()
        paciente = Paciente(
            rut=datos["rut"],
            nombre=datos["nombre"],
            apellido=datos["apellido"],
            edad=datos["edad"],
            genero=datos["genero"],
            telefono=datos["telefono"],
            correo=datos["correo"],
            direccion=datos["direccion"]
        )
        sesion.add(paciente)
        sesion.commit()
        return {"mensaje": "Paciente agregado correctamente"}
    except Exception as e:
        sesion.rollback()
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint para listar pacientes
@router.get("/ListaPacientes")
def obtener_pacientes(
    sesion: Session = Depends(obtener_sesion), 
    datos_token: Dict[str, Any] = Depends(verificar_token)
) -> list[Dict[str, Any]]:
    try:
        pacientes = sesion.query(Paciente).all()
        return [{
            "rut": p.rut,
            "nombre": p.nombre,
            "apellido": p.apellido,
            "edad": p.edad,
            "genero": p.genero,
            "telefono": p.telefono,
            "correo": p.correo,
            "direccion": p.direccion
        } for p in pacientes]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint para eliminar paciente
# apliacion de tiny hints para que el codigo sea mas legible



@router.delete("/EliminarPaciente/{rut_paciente}")
def eliminar_paciente(
    rut_paciente: str, 
    sesion: Session = Depends(obtener_sesion), 
    datos_token: Dict[str, Any] = Depends(verificar_token)
) -> Dict[str, str]:
    try:
        paciente = sesion.query(Paciente).filter(Paciente.rut == rut_paciente).first()
        if not paciente:
            raise HTTPException(status_code=404, detail="Paciente no encontrado")
        
        sesion.delete(paciente)
        sesion.commit()
        return {"mensaje": "Paciente eliminado correctamente"}
    except Exception as e:
        sesion.rollback()
        raise HTTPException(status_code=400, detail=str(e))