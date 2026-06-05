from config.database import Base
from sqlalchemy import String, Column, Integer, Date, Time, ForeignKey, Enum
from sqlalchemy.orm import relationship

class Turno(Base):
    __tablename__ = "Turno"

    id_turno = Column(Integer, primary_key=True, autoincrement= True)
    fecha_turno = Column(Date, nullable= False)
    hora_turno = Column(Time, nullable= False)
    id_cliente = Column(Integer, ForeignKey("Cliente.id_cliente"), ondelete= "CASCADE", nullable= False)
    id_servicio = Column(Integer, ForeignKey("Servicio.id_servicio"), ondelete = "CASCADE", nullable= False )
    id_barbero = Column(String(100), ForeignKey("Barbero.id_barbero"), ondelete = "CASCADE", nullable= False )
    estado = Column(Enum('Pendiente','Cancelado','Realizado', name= 'estados_turno'), nullable=False)

    cliente = relationship("Cliente", back_populates="turno")
    Servicio = relationship("Servicio", back_populates="turno")
    barbero = relationship("Barbero", back_populates="turno")