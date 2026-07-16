from sqlalchemy.orm import Session
from models.turno import Turno
from exceptions.turno_exceptions import NoExisteTurno, TurnoNoSeCreo, TurnoNoSeEdito, TurnoNoSeElimino, TurnoNoSeModificoEstado 
from fastapi import HTTPException
from schemas.s_turno import TurnoCreate, TurnoEstado, TurnoEstadoCancelado, TurnoEstadoRealizado, TurnoResponse, TurnoUpdate
from sqlalchemy.exc import SQLAlchemyError

def get_turnos_service(db: Session):
    return db.query(Turno).all()

def get_turno_service(id_turno : int ,db : Session):
    turno = db.query(Turno).filter(
        Turno.id_turno == id_turno
    ).first()

    if not turno:
        raise NoExisteTurno(id_turno)
    
    return turno

def create_turno_service(turno: TurnoCreate, db: Session):
    new_turno = Turno(
        fecha_turno = turno.fecha_turno,
        hora_turno = turno.hora_turno,
        id_servicio = turno.id_servicio,
        id_barbero = turno.id_barbero,
        estado = turno.estado,
        nombre_cliente = turno.nombre_cliente,
        telefono_cliente = turno.telefono_cliente
    )

    try:
        db.add(new_turno)
        db.commit()
        db.refresh(new_turno)

    except SQLAlchemyError:
        db.rollback()
        raise TurnoNoSeCreo()
    
    return new_turno


def update_turno_service(id_turno: int, turno : TurnoUpdate, db: Session):
    existe = db.query(Turno).filter(
        Turno.id_turno == id_turno
    ).first()

    if not existe:
        raise NoExisteTurno(id_turno)
    
    if turno.fecha_turno is not None:
        existe.fecha_turno = turno.fecha_turno
    if turno.hora_turno is not None:
        existe.hora_turno = turno.hora_turno
    if turno.id_servicio is not None: 
        existe.id_servicio = turno.id_servicio
    if turno.id_barbero is not None:
        existe.id_barbero = turno.id_barbero
    if turno.nombre_cliente is not None:
        existe.nombre_cliente = turno.nombre_cliente
    if turno.telefono_cliente is not None:
        existe.telefono_cliente = turno.telefono_cliente
    
    try:
        db.commit()
        db.refresh(existe)
    except SQLAlchemyError:
        db.rollback()
        raise TurnoNoSeEdito(id_turno)
    

    return existe


def update_estado_cancelado_service(id_turno:int, estado_cancelado: TurnoEstado, db: Session):
    existe = db.query(Turno).filter(
        Turno.id_turno == id_turno
    ).first()

    if not existe:
        raise NoExisteTurno(id_turno)
    
    if estado_cancelado.estado is not None:
        existe.estado = estado_cancelado.estado
    
    try:
        db.commit()
        db.refresh(existe)
    except SQLAlchemyError:
        db.rollback()
        raise TurnoNoSeModificoEstado(id_turno)
    
    return existe

def update_estado_realizado_service(id_turno:int, estado_realizado : TurnoEstadoRealizado, db: Session):
    existe = db.query(Turno).filter(
        Turno.id_turno == id_turno
    ).first()

    if not existe:
        raise NoExisteTurno(id_turno)
    
    if estado_realizado.estado is not None:
        existe.estado = estado_realizado.estado
    
    try:
        db.commit()
        db.refresh(existe)
    except SQLAlchemyError:
        db.rollback()
        raise TurnoNoSeModificoEstado(id_turno)
    
    return existe

def delete_turno_service(id_turno: int, db : Session):
    existe = db.query(Turno).filter(
        Turno.id_turno == id_turno
    ).first()

    if not existe:
        raise NoExisteTurno(id_turno)
    
    try:
        db.delete(existe)
        db.commit()
    except SQLAlchemyError:
        db.rollback()
        raise TurnoNoSeElimino(id_turno)
