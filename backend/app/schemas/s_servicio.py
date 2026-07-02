from pydantic import BaseModel, ConfigDict
from typing import Optional

class ServicioCreate(BaseModel):
    nombre_servicio : str
    valor_servicio : float

class ServicioUpdate(BaseModel):
    nombre_servicio : Optional[str] = None
    valor_servicio : Optional[float] = None

class ServicioResponse(ServicioCreate):
    id_servicio: int

    model_config = ConfigDict(from_attributes = True)

