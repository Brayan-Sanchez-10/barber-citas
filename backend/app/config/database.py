from sqlalchemy import create_engine #permite crear una conexion entre python y la base de datos

from sqlalchemy.orm import sessionmaker, declarative_base #sessionmaker sirve para crear sesiones de base de datos, 
#lo que permite consultar, insertar, actualizar y eliminar datos; 
#declarative_base sirve para crear una clase base de a que heredaran todos los modelos 

from dotenv import load_dotenv # importa la funcion que permite leer variables de entorno desde un archivo .env

import os # importamos el modulo de python para trabajar con el sistema operativo

load_dotenv() #Lee todas las variables almacenadas en el archivo .env

DATABASE_URL = os.getenv("DATABASE_URL"
) #busca una variable llamada DATABASE_URL y guarda su valor

engine = create_engine(DATABASE_URL) #Creamos el obajeto principal que administra la conexion con la db.

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False) #Declaramos la forma general de crear sesiones. bind=engine: todas las sesiones usaran este engine, autocommit=false los cambios No se guardan automaticamente; autoflush=false evitar que SQLAlchemy envie cambios automaticamente a la db

Base = declarative_base() # Es la clase padre de todos los modelos, permite que SQLAlchemy convoerta clases en tablas.

def get_db(): # esta funcion crea y devuelve una sesion de base de datos.
    db = SessionLocal()
    print("sesion creada")
    try:
        yield db
    finally:
        print("sesion cerrada")
        db.close()