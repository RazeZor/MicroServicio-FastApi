from fastapi import APIRouter, Depends, Request, HTTPException, status
from sqlalchemy.orm import Session
from models.modelos import Formulario
from typing import Dict, Any
from DB.dependencias import obtener_sesion, verificar_token

router = APIRouter(tags=["formularios"])

@router.post("/formularios")
async def crear_formulario(
    solicitud: Request,
    sesion: Session = Depends(obtener_sesion),
    datos_token: Dict[str, Any] = Depends(verificar_token)
) -> Dict[str, str]:
    try:
        datos = await solicitud.json()

        nuevo_formulario = Formulario(
            rut_paciente=datos["rut_paciente"],
            respuesta1=datos["respuesta1"],
            respuesta2=datos["respuesta2"],
            respuesta3=datos["respuesta3"]
        )

        sesion.add(nuevo_formulario)
        sesion.commit()
        return {"mensaje": "Formulario creado correctamente"}

    except Exception as e:
        sesion.rollback()
        raise HTTPException(status_code=400, detail=str(e))
