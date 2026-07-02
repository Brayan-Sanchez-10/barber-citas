from fastapi import APIRouter, Depends, HTTPException, status
from schemas. s_servicio import ServicioCreate, ServicioResponse, ServicioUpdate
from sqlalchemy.orm import Session
from config.database import get_db
from exceptions.servicio_exceptions import NoExisteServicio, ServicioNoSeCreo, ServicioNoSeActualizo, ServicioNoSeElimino
from services.ser_servicio import get_servicios_service, get_servicio_service, create_servicio_service, update_servicio_service, delete_servicio_service

router = APIRouter(
    prefix="/servicios",
    tags=["Servicios"]
)

@router.get("", response_model= list[ServicioResponse])
def get_servicios_router(db : Session = Depends (get_db)):
    return get_servicios_service(db = db)

@router.get("/{id_servicio}", response_model= ServicioResponse)
def get_servicio_router(id_servicio : int, db :Session = Depends (get_db)):
    try: 
        return get_servicio_service(id_servicio, db = db)
    
    except NoExisteServicio as e:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail= str(e) 
        )

@router.post("", response_model= ServicioResponse)
def create_servicio_router(servicio: ServicioCreate, db:  Session= Depends(get_db)):
    try:
        return create_servicio_service(servicio, db = db)
    
    except ServicioNoSeCreo as e:
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail= str(e)
        )
    

@router.put("/{id_servicio}", response_model= ServicioResponse)
def update_servicio_router(id_servicio: int, servicio : ServicioUpdate, db : Session= Depends(get_db)):
    try:
        return update_servicio_service(id_servicio, servicio, db = db)
    
    except NoExisteServicio as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= str(e)
        ) 
    
    except ServicioNoSeActualizo as e:
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail= str(e)
        )

@router.delete("/{id_servicio}")
def delete_servicio_router(id_servicio: int, db: Session = Depends(get_db)):
    try: 
        return delete_servicio_service(id_servicio, db = db)
    
    except NoExisteServicio as e:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= str(e)
        )
    
    except ServicioNoSeElimino as e:
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail= str(e)
        )
    