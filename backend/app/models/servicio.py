from config.database import Base
from sqlalchemy import String, column, Integer, Numeric
from sqlalchemy.orm import relationship

class Servicio(Base):
    __tablename__ = "Servicio"

    id_servicio = column(Integer, primary_key = True, autoincrement= True)
    nombre_servicio = column(String(100), nullable = False)
    valor_servicio =  column(Numeric(10, 2), nullable = False)

    turno = relationship("Turno", back_populates="servicio")

