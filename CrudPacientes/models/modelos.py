from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base
from dataclasses import dataclass


@dataclass
class Paciente(Base):
    __tablename__ = "pacientes"
    rut = Column(String(15), primary_key=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    edad = Column(Integer, nullable=False)
    genero = Column(String(10), nullable=False)
    telefono = Column(String(15), nullable=False)
    correo = Column(String(50), unique=True, nullable=False)
    direccion = Column(String(100), nullable=False)
    
    formularios = relationship("Formulario", back_populates="paciente", cascade="all, delete-orphan")

@dataclass
class Formulario(Base):
    __tablename__ = "formularios"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    rut_paciente = Column(String(15), ForeignKey("pacientes.rut"), nullable=False)
    respuesta1 = Column(String(17), nullable=False)
    respuesta2 = Column(String(17), nullable=False)
    respuesta3 = Column(String(17), nullable=False)
    
    paciente = relationship("Paciente", back_populates="formularios")

