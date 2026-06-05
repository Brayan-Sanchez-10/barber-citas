from config.database import Base
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship

class Cliente(Base):
    __tablename__ = "Cliente"

    id_cliente= Column(Integer, primary_key= True, autoincrement=True)
    nombre_cliente= Column(String(100), nullable=False)
    telefono_cliente= Column(String(100), nullable=False)

    turno = relationship("Turno", back_populates="Cliente")