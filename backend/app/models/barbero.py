from config.database import Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship

class Barbero(Base):
    __tablename__ = "Barbero"

    id_barbero = Column(String(20), primary_key = True)
    nombre_barbero = Column(String(100), nullable= False)
    telefono_barbero = Column(String(100), nullable= False)
    contrasena_barbero = Column(String(100), nullable= False)

    turno = relationship("Turno", back_populates="barbero")