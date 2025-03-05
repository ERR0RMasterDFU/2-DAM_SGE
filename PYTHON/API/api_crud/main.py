import os
from fastapi import FastAPI 
from routers import producto, producto_db
from db import model, database
from db.database import engine

app = FastAPI()

# CREA LAS TABLAS Y EJECUTA EL "import.sql" SÓLO SI NO EXISTE EL ARCHIVO "database.db"
def initialize_db():
    if not os.path.exists('db/database.db'):
        print("Inicializando la base de datos...")
        model.Base.metadata.create_all(bind=engine)
        database.run_import_sql()
    else:
        print("La base de datos ya está creada, no es necesario inicializarla.")


initialize_db() 

app.include_router(producto.router)
app.include_router(producto_db.router)


### PASOS A SEGUIR ###

# 1- INSTALAR PIP
# 2- INSTALAR FAST API:     pip install "fastapi[all]"
# 3- INSTALAR SQL ALCHEMY:  pip install sqlalchemy psycopg2-binary
# 4- INICIA EL SERVIDOR:    uvicorn main:app --reload