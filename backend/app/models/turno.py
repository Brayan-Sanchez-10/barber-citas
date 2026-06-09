import uuid
from config.database import Base
from sqlalchemy import String, Column, Integer, Date, Time, ForeignKey, Enum, Uuid
from sqlalchemy.orm import relationship

class Turno(Base):
    __tablename__ = "Turno"

    id_turno = Column(Uuid, primary_key=True, default= uuid.uuid4())
    fecha_turno = Column(Date, nullable= False)
    hora_turno = Column(Time, nullable= False)
    id_servicio = Column(Integer, ForeignKey("Servicio.id_servicio"), ondelete = "CASCADE", nullable= False )
    id_barbero = Column(String(100), ForeignKey("Barbero.id_barbero"), ondelete = "CASCADE", nullable= False )
    estado = Column(Enum('Pendiente','Cancelado','Realizado', name= 'estados_turno'), nullable=False)
    nombre_cliente = Column(String, nullable= False)
    telefono_cliente = Column(String, nullable= False)

    Servicio = relationship("Servicio", back_populates="turno")
    barbero = relationship("Barbero", back_populates="turno")