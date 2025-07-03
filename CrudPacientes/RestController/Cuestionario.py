from fastapi import APIRouter, Depends, Request, HTTPException, status
from sqlalchemy.orm import Session
from models.modelos import Formulario
from typing import Dict, Any
from DB.dependencias import obtener_sesion, verificar_token
from models.modelos import Paciente

router = APIRouter(tags=["formularios"])

@router.post("/formularios")
async def crear_formulario(
    solicitud: Request,
    sesion: Session = Depends(obtener_sesion),
    datos_token: Dict[str, Any] = Depends(verificar_token)
) -> Dict[str, str]:
    try:
        datos = await solicitud.json()
        errores = []
        
        campos_obligatorios = ["rut_paciente", "respuesta1", "respuesta2", "respuesta3"]
        for campo in campos_obligatorios:
            if campo not in datos or not datos[campo]:
                errores.append(f"El campo '{campo}' es obligatorio y no fue proporcionado.")

        if errores:
            raise HTTPException(status_code=422, detail=errores)

        paciente = sesion.query(Paciente).filter_by(rut=datos["rut_paciente"]).first()
        if not paciente:
            raise HTTPException(status_code=404, detail=f"Paciente con RUT {datos['rut_paciente']} no encontrado.")

        nuevo_formulario = Formulario(
            rut_paciente=datos["rut_paciente"],
            respuesta1=datos["respuesta1"],
            respuesta2=datos["respuesta2"],
            respuesta3=datos["respuesta3"]
        )

        sesion.add(nuevo_formulario)
        sesion.commit()
        return {"mensaje": "Formulario creado correctamente"}

    except HTTPException:
        raise 
    except Exception as e:
        sesion.rollback()
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")
