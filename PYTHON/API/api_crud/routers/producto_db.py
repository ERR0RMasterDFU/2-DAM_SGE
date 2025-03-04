from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import SessionLocal
from routers import producto_db
from routers.producto import Producto


router = APIRouter(
    prefix="/productoDB", 
    tags=["producto_db"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

"""
@router.get("/")
async def get_all_productos(db: db_dependency):
    return db.query(producto_db).all()


@router.get("/{id}")
async def get_producto(id: int, db: db_dependency):
    producto = db.query(producto_db).filter(producto_db.id == id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto


@router.post("/", status_code=201)
async def create_producto(producto: Producto, db: db_dependency):
    if db.query(producto_db).filter(producto_db.nombre == producto.nombre).first():
        raise HTTPException(status_code=409, detail="Ya existe un producto con ese nombre")

    nuevo_producto = producto_db(nombre=producto.nombre, precio=producto.precio, en_oferta=producto.en_oferta)
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto


@router.put("/{id}", status_code=200)
async def update_producto(id: int, producto: Producto, db: db_dependency):
    producto_db = db.query(producto_db).filter(producto_db.id == id).first()
    if not producto_db:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    producto_db.nombre = producto.nombre
    producto_db.precio = producto.precio
    producto_db.en_oferta = producto.en_oferta

    db.commit()
    db.refresh(producto_db)
    return producto_db


@router.delete("/{id}", status_code=204)
async def delete_producto(id: int, db: db_dependency):
    producto = db.query(producto_db).filter(producto_db.id == id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    db.delete(producto)
    db.commit()
"""