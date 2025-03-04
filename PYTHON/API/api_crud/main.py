from fastapi import FastAPI 
from routers import producto, producto_db
from db import model
from db.database import engine

app = FastAPI()
model.Base.metadata.create_all(bind=engine)

app.include_router(producto.router)
app.include_router(producto_db.router)





# INICIA EL SERVIDOR: uvicorn producto:app --reload

### PASOS A SEGUIR ###

# 1- INSTALAR PIP
# 2- INSTALAR FAST API:     pip install "fastapi[all]"
# 3- INSTALAR SQL ALCHEMY:  pip install sqlalchemy psycopg2-binary