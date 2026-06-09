import uuid
from config.database import Base
from sqlalchemy import String, Column, Numeric, Uuid
from sqlalchemy.orm import relationship

class Servicio(Base):
    __tablename__ = "Servicio"

    id_servicio = Column(Uuid, primary_key = True, defaulth = uuid.uuid4())
    nombre_servicio = Column(String(100), nullable = False)
    valor_servicio =  Column(Numeric(10, 2), nullable = False)

    turno = relationship("Turno", back_populates="servicio")

