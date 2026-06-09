from pydantic import BaseModel, ConfigDict, UUID4
from typing import Optional

class ServicioCreate(BaseModel):
    nombre_servicio : str
    valor_servicio : float

class ServicioUpdate(BaseModel):
    nombre_servicio : Optional[str] = None
    valor_servicio : Optional[float] = None

class ServicioDelete(BaseModel):
    id_servicio : UUID4

class ServicioResponse(ServicioCreate):
    id_servicio: UUID4

    model_config = ConfigDict(from_attributes = True)

