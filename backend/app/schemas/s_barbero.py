from pydantic import BaseModel, Field, ConfigDict, model_validator
from typing import Optional

class BarberoCreate(BaseModel):
    id_barbero : str
    nombre_barbero : str
    telefono_barbero: str
    contrasena_barbero: str = Field(min_length=8)

class BarberoUpdate(BaseModel):
    nombre_barbero: Optional[str] = None
    telefono_barbero: Optional[str] = None

class BarberoUpdateContrasena (BaseModel):
    contrasena_actual: str
    nueva_contrasena: str = Field(min_length=8)
    confirmacion_contrasena: str

    @model_validator(mode='after')
    def verificar_coincidencia(self):
        if self.nueva_contrasena != self.confirmacion_contrasena:
            raise ValueError("La contraseña nueva no es igual a la confirmacion")
        return self

class BarberoDelete(BaseModel):
    id_barbero : str
    contrasena_confirmacion : str

class BarberoResponse(BaseModel):
    id_barbero : str
    nombre_barbero : str
    telefono_barbero : str
    
    model_config = ConfigDict(from_attributes=True)