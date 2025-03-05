from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from db.database import SessionLocal
from db.model import Producto_tabla 
from routers.producto import Producto


### ROUTER -----------------------------------------------------------------------------------------------------------------------------------------------------------

router = APIRouter(
    prefix="/productoDB", 
    tags=["producto_db"],
)


### DTO DE RESPUESTA (PORQUE SI NO SALE DESORDENADO) -----------------------------------------------------------------------------------------------------------------

class GetProductoDto(BaseModel):
    id: int
    nombre: str
    precio: float
    en_oferta: bool

    class Config:
        orm_mode = True


### SESIÓN Y BASE DE DATOS -------------------------------------------------------------------------------------------------------------------------------------------

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


### ENDPOINTS --------------------------------------------------------------------------------------------------------------------------------------------------------

# OBTENER TODOS LOS PRODUCTOS (findAll)
@router.get("/", response_model=List[GetProductoDto])
async def get_all_productos(db: db_dependency):
    return db.query(Producto_tabla).all()


# OBTENER UN PRODUCTO POR ID (findById)
@router.get("/{id}", response_model=GetProductoDto)
async def get_producto(id: int, db: db_dependency):
    producto = db.query(Producto_tabla).filter(Producto_tabla.id == id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto


# CREAR UN NUEVO PRODUCTO (save)
@router.post("/", status_code=201, response_model=GetProductoDto)
async def create_producto(producto: Producto, db: db_dependency):
   
    if db.query(Producto_tabla).filter(Producto_tabla.nombre == producto.nombre).first():
        raise HTTPException(status_code=409, detail="Ya existe un producto con ese nombre")

    nuevo_producto = Producto_tabla(
        nombre=producto.nombre, 
        precio=producto.precio, 
        en_oferta=producto.en_oferta
    )
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto


# EDITAR UN PRODUCTO POR ID (save / edit)
@router.put("/{id}", status_code=200, response_model=GetProductoDto)
async def update_producto(id: int, producto: Producto, db: db_dependency):
    producto_db = db.query(Producto_tabla).filter(Producto_tabla.id == id).first()
    if not producto_db:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    producto_db.nombre = producto.nombre
    producto_db.precio = producto.precio
    producto_db.en_oferta = producto.en_oferta
    db.commit()
    db.refresh(producto_db)
    return producto_db


# BORRAR UN PRODUCTO POR ID (delete)
@router.delete("/{id}", status_code=204)
async def delete_producto(id: int, db: db_dependency):
    producto = db.query(Producto_tabla).filter(Producto_tabla.id == id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    db.delete(producto)
    db.commit()
