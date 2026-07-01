from fastapi import APIRouter, HTTPException, Depends, status
from schemas.s_barbero import BarberoCreate, BarberoDelete, BarberoResponse, BarberoUpdate, BarberoUpdateContrasena
from config.database import get_db
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.barbero import Barbero
from app.exceptions import NoExisteBarbero, YaExisteBarberoConEseID, ContrasenaIncorrecta,  ContrasenaNoSeActualizo, BarberoNoSeElimino, BarberoNoSeActualizo, BarberoNoSeCreo
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_barberos_service(db: Session):
    return db.query(Barbero).all()

def get_barbero_service(id_barbero: str, db: Session):
    barbero = db.query(Barbero).filter(
        Barbero.id_barbero == id_barbero
    ).first()

    if not barbero:
        raise NoExisteBarbero(id_barbero)
    
    return barbero

def create_barbero_service(barbero: BarberoCreate, db: Session):
    existe = db.query(Barbero).filter(
        Barbero.id_barbero == barbero.id_barbero 
    ).first()

    if existe:
        raise YaExisteBarberoConEseID(barbero.id_barbero)
    
    contrasena_haseada = pwd_context.hash(barbero.contrasena_barbero)

    new_barbero = Barbero(
        id_barbero = barbero.id_barbero,
        nombre_barbero= barbero.nombre_barbero,
        telefono_barbero= barbero.telefono_barbero,
        contrasena_barbero= contrasena_haseada
    )

    try:
        db.add(new_barbero)
        db.commit()
        db.refresh(new_barbero)
    except SQLAlchemyError:
        db.rollback()
        raise BarberoNoSeCreo

    return new_barbero

def update_barbero_service(id_barbero: str, barbero: BarberoUpdate, db: Session):
    existe = db.query(Barbero).filter(
        Barbero.id_barbero == id_barbero
    ).first()

    if not existe:
        raise NoExisteBarbero(id_barbero)
    
    if barbero.nombre_barbero:
        existe.nombre_barbero = barbero.nombre_barbero
    if barbero.telefono_barbero:
        existe.telefono_barbero = barbero.telefono_barbero
    
    try:
        db.commit()
        db.refresh(existe)

    except SQLAlchemyError:
        db.rollback()
        raise BarberoNoSeActualizo(id_barbero)
    
    return existe

def update_contrasena_barbero_service(id_barbero: str, data_contrasena: BarberoUpdateContrasena, db:Session):
    existe = db.query(Barbero).filter(
        Barbero.id_barbero == id_barbero
    ).first()

    if not existe:
        raise NoExisteBarbero(id_barbero)
    
    if not pwd_context.verify(data_contrasena.contrasena_actual, existe.contrasena_barbero):
        raise ContrasenaIncorrecta
    
    
    existe.contrasena_barbero = pwd_context.hash(data_contrasena.nueva_contrasena)
    
    
    try:
        db.commit()
        db.refresh(existe)
    
    except SQLAlchemyError:
        db.rollback()
        raise ContrasenaNoSeActualizo

    return existe

    
def delete_barbero_service(data_delete: BarberoDelete, db : Session):
    existe = db.query(Barbero).filter(
        Barbero.id_barbero == data_delete.id_barbero
    ).first()

    if not existe:
        raise NoExisteBarbero(data_delete.id_barbero)
    
    if not pwd_context.verify(data_delete.contrasena_confirmacion, existe.contrasena_barbero):
        raise ContrasenaIncorrecta

    try:
        db.delete(existe)
        db.commit()
    
    except SQLAlchemyError:
        db.rollback()
        raise BarberoNoSeElimino(data_delete.id_barbero)
    
    

    






