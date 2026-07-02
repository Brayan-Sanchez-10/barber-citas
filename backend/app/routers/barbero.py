from fastapi import APIRouter, status, HTTPException, Depends
from schemas.s_barbero import BarberoCreate, BarberoDelete, BarberoResponse, BarberoUpdate, BarberoUpdateContrasena
from sqlalchemy.orm import Session
from config.database import get_db
from services.ser_barbero import get_barberos_service, get_barbero_service, create_barbero_service, update_barbero_service, update_contrasena_barbero_service, delete_barbero_service
from exceptions.barbero_exceptions import NoExisteBarbero, YaExisteBarberoConEseID, ContrasenaIncorrecta, ContrasenaNoCoinciden, ContrasenaNoSeActualizo, BarberoNoSeElimino, BarberoNoSeCreo, BarberoNoSeActualizo
router = APIRouter(
    prefix="/barberos",
    tags=["Barberos"]
)


@router.get("", response_model=list[BarberoResponse])
def get_barberos_router(db: Session = Depends(get_db)):
    return get_barberos_service(db=db)
    

@router.get("/{id_barbero}", response_model= BarberoResponse)
def get_barbero_router(id_barbero: str , db: Session = Depends(get_db)):

    try:    
        return get_barbero_service(id_barbero, db=db)
    except NoExisteBarbero as e:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

@router.post("", response_model= BarberoResponse)
def create_barbero_router(barbero: BarberoCreate, db : Session = Depends(get_db)):
    try:
        return create_barbero_service(barbero, db = db)
    
    except YaExisteBarberoConEseID as e:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail= str(e)
        )
    
    except BarberoNoSeCreo as e:
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail= str(e)
        )

@router.put("/{id_barbero}", response_model= BarberoResponse)
def update_barbero_router(id_barbero: str, barbero: BarberoUpdate, db: Session = Depends(get_db)):
    try:
        return update_barbero_service(id_barbero, barbero, db = db)
    
    except NoExisteBarbero as e:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= str(e)
        )
    
    except BarberoNoSeActualizo as e:
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail= str(e)
        )
    
@router.patch("/{id_barbero}/contrasena", response_model= BarberoResponse)
def update_contrasena_barbero_router(id_barbero: str, data_contrasena: BarberoUpdateContrasena, db :Session = Depends(get_db)):
    try:
        return update_contrasena_barbero_service(id_barbero, data_contrasena, db=db)
    
    except ContrasenaNoCoinciden as e:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    
    except ContrasenaIncorrecta as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    
    except ContrasenaNoSeActualizo as e:
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail= str(e)
        )
    
    except NoExisteBarbero as e:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= str(e)
        )
    
@router.delete("")
def delete_barbero_router(data_delete : BarberoDelete, db : Session = Depends(get_db)):
    try:
        return delete_barbero_service(data_delete , db = db)
    
    except NoExisteBarbero as e:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= str(e)
        )

    except ContrasenaIncorrecta as e:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail= str(e)
        )
    
    except BarberoNoSeElimino as e:
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail= str(e)
        )
    
    
