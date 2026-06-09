from pydantic import BaseModel, ConfigDict, UUID4
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
    id_servicio : UUID4
    id_barbero : str
    estado : TurnoEstado = TurnoEstado.pendiente
    nombre_cliente : str
    telefono_cliente : str

class TurnoUpdate(BaseModel):
    fecha_turno: Optional[date] = None
    hora_turno : Optional[time] = None
    nombre_cliente : Optional[str] = None
    telefono_cliente: Optional [str] = None

class TurnoEstadoCancelado(BaseModel):
    estado : TurnoEstado = TurnoEstado.cancelado
class TurnoEstadoRealizado(BaseModel):
    estado : TurnoEstado = TurnoEstado.realizado 

class TurnoDelete(BaseModel):
    id_turno : UUID4


class TurnoResponse(TurnoCreate):
    id_turno : UUID4

    model_config =  ConfigDict(from_attributes= True)
