from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from services.ser_turno import get_turnos_service, get_turno_service,  create_turno_service, update_turno_service, update_estado_cancelado_service
from schemas.s_turno import TurnoCreate, TurnoDelete, TurnoEstadoCancelado, TurnoEstadoRealizado, TurnoResponse, TurnoUpdate
from config.database import get_db
from exceptions.turno_exceptions import NoExisteTurno, TurnoNoSeCreo, TurnoNoSeEdito, TurnoNoSeModificoEstado


router = APIRouter(
    prefix = "/turnos",
    tags= ["Turnos"]
)

@router.get("", response_model= list[TurnoUpdate])
def get_turnos_router(db : Session = Depends(get_db)):
    return get_turnos_service(db = db)


@router.get("{id_turno}", response_model = TurnoResponse)
def get_turno_router(id_turno : int, db : Session =Depends(get_db)):
    try:
        return get_turno_service(id_turno, db = db)
    
    except NoExisteTurno as e:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= str(e)
        )

@router.post("", response_model= TurnoResponse)
def create_turno_router(turno: TurnoCreate, db: Session = Depends(get_db)):
    try:
        return create_turno_service(turno, db = db)
    
    except TurnoNoSeCreo as e:
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail= str(e)
        )


@router.put("{id_turno}", response_model= TurnoResponse)
def update_turno_router(id_turno: int,turno: TurnoUpdate, db : Session = Depends(get_db)):
    try:
        return update_turno_service(turno, db=db)
    
    except NoExisteTurno as e:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= str(e)
        )
    
    except TurnoNoSeEdito as e:
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail= str(e)
        )
    
@router.patch("{id_turno}/cancelado", response_model= TurnoResponse)
def update_estado_cancelado_router(estado : TurnoEstadoCancelado, db: Session= Depends(get_db)):
    try:
        return update_estado_cancelado_service( estado, db = db)
    
    except NoExisteTurno as e:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= str(e)
        )
    
    except TurnoNoSeModificoEstado as e:
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail= str(e)
        )

@router.patch("{id_turno}/realizado", response_model= TurnoResponse)
def update_estado_realizado_router(estado: TurnoEstadoRealizado, db : Session = Depends(get_db)):
    pass