from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.servicio import Servicio
from exceptions.servicio_exceptions import ServicioNoSeActualizo,ServicioNoSeCreo,ServicioNoSeElimino,NoExisteServicio
from schemas.s_servicio import ServicioCreate, ServicioUpdate


def get_servicios_service(db: Session):
    return db.query(Servicio).all()   

def get_servicio_service(id_servicio: int, db : Session):
    existe = db.query(Servicio).filter(
        Servicio.id_servicio == id_servicio
    ).first()

    if not existe:
        raise NoExisteServicio(id_servicio)
    
    return existe

def create_servicio_service(servicio: ServicioCreate, db : Session):

    new_servicio = Servicio(
        nombre_servicio = servicio.nombre_servicio,
        valor_servicio = servicio.valor_servicio
    )
    try:
        db.add(new_servicio)
        db.commit()
        db.refresh(new_servicio)
    except SQLAlchemyError:
        db.rollback()
        raise ServicioNoSeCreo
    
    return new_servicio

def update_servicio_service(id_servicio : int, servicio : ServicioUpdate, db: Session):
    existe = db.query(Servicio).filter(
        Servicio.id_servicio == id_servicio
    ).first()

    if not existe:
        raise NoExisteServicio(id_servicio)
    
    if servicio.nombre_servicio is not None:
        existe.nombre_servicio = servicio.nombre_servicio
    if servicio.valor_servicio is not None:
        existe.valor_servicio = servicio.valor_servicio
    
    try :
        db.commit()
        db.refresh(existe)
    
    except SQLAlchemyError:
        db.rollback()
        raise ServicioNoSeActualizo(id_servicio)
    
    return existe

def delete_servicio_service(id_servicio : int, db : Session):
    existe = db.query(Servicio).filter(
        Servicio.id_servicio == id_servicio
    ).first()

    if not existe:
        raise NoExisteServicio(id_servicio)
    
    try:
        db.delete(existe)
        db.commit()
    
    except SQLAlchemyError:
        db.rollback()
        raise ServicioNoSeElimino(id_servicio)
    