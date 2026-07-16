from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, time
from enum import Enum

class TurnoEstado(str, Enum):
    pendiente = "Pendiente"
    cancelado = "Cancelado"
    realizado = "Realizado"

class TurnoCreate(BaseModel):
    fecha_turno : date
    hora_turno : time
    id_servicio : int
    id_barbero : str
    estado : TurnoEstado = TurnoEstado.pendiente
    nombre_cliente : str
    telefono_cliente : str

class TurnoUpdate(BaseModel):
    fecha_turno: Optional[date] = None
    hora_turno : Optional[time] = None
    id_servicio : Optional[int] = None
    id_barbero : Optional[str] = None
    nombre_cliente : Optional[str] = None
    telefono_cliente: Optional [str] = None

class TurnoEstadoCancelado(BaseModel):
    estado : TurnoEstado = TurnoEstado.cancelado
class TurnoEstadoRealizado(BaseModel):
    estado : TurnoEstado = TurnoEstado.realizado 

class TurnoResponse(TurnoCreate):
    id_turno : int

    model_config =  ConfigDict(from_attributes= True)
