from pydantic import BaseModel, Field, ConfigDict, model_validator
from typing import Optional
from exceptions.barbero_exceptions import ContrasenaNoCoinciden

class BarberoCreate(BaseModel):
    id_barbero : str
    nombre_barbero : str
    telefono_barbero: str
    contrasena_barbero: str = Field(min_length=8) #Field sistema de validacion que en este caso dice que minimo 8 caracteres debe de incluir la contraseña

class BarberoUpdate(BaseModel):
    nombre_barbero: Optional[str] = None
    telefono_barbero: Optional[str] = None

class BarberoUpdateContrasena (BaseModel):
    contrasena_actual: str
    nueva_contrasena: str = Field(min_length=8)
    confirmacion_contrasena: str

    @model_validator(mode='after') #validacion automatica para que despues de validar los datos se valide la semenjanza de la nueva contraseña y su confirmacion
    def verificar_coincidencia(self):
        if self.nueva_contrasena != self.confirmacion_contrasena:
            raise ContrasenaNoCoinciden
        return self

class BarberoDelete(BaseModel):
    id_barbero : str
    contrasena_confirmacion : str

class BarberoResponse(BaseModel):
    id_barbero : str
    nombre_barbero : str
    telefono_barbero : str
    
    model_config = ConfigDict(from_attributes=True)