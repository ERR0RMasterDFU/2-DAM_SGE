from typing import Optional
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


### ROUTER -----------------------------------------------------------------------------------------------------------------------------------------------------------

router = APIRouter(
    prefix="/producto", 
    tags=["producto"], 
    responses={404: {"message": "No se han encontrado productos"}}
)


### CLASE MODELO -----------------------------------------------------------------------------------------------------------------------------------------------------

class Producto(BaseModel):
    id: Optional[int] = None  # EL ID PUEDE SER NONE (NO SE INTRODUCE EN EL REQUEST BODY)
    nombre: str
    precio: float
    en_oferta: bool


### LISTA DE PRODUCTOS (SIMULADOR DE "import.sql") -------------------------------------------------------------------------------------------------------------------

lista_productos = [
    Producto(id=1, nombre="Sopa de tomate", precio=2.50, en_oferta=True),
    Producto(id=2, nombre="Botella de agua", precio=1.00, en_oferta=False),
    Producto(id=3, nombre="Pasta carbonara", precio=3.75, en_oferta=True),
    Producto(id=4, nombre="Cereales de avena", precio=4.20, en_oferta=False),
    Producto(id=5, nombre="Galletas de chocolate", precio=2.80, en_oferta=True),
    Producto(id=6, nombre="Zumo de naranja", precio=3.10, en_oferta=False),
    Producto(id=7, nombre="Pan integral", precio=1.50, en_oferta=True),
    Producto(id=8, nombre="Arroz basmati", precio=2.90, en_oferta=False),
    Producto(id=9, nombre="Croquetas", precio=5.60, en_oferta=True),
    Producto(id=10, nombre="Queso cheddar", precio=6.25, en_oferta=False),
    Producto(id=11, nombre="Mermelada de fresa", precio=3.45, en_oferta=True),
    Producto(id=12, nombre="Yogur natural", precio=1.20, en_oferta=False),
    Producto(id=13, nombre="Aceite de oliva", precio=7.80, en_oferta=True),
    Producto(id=14, nombre="Chocolate negro", precio=2.99, en_oferta=False),
    Producto(id=15, nombre="Café en grano", precio=8.50, en_oferta=True),
    Producto(id=16, nombre="Té verde", precio=4.75, en_oferta=False),
    Producto(id=17, nombre="Garbanzos enlatados", precio=1.90, en_oferta=True),
    Producto(id=18, nombre="Harina de trigo", precio=2.20, en_oferta=False),
    Producto(id=19, nombre="Miel", precio=5.30, en_oferta=True),
    Producto(id=20, nombre="Sal marina", precio=1.80, en_oferta=False),
]


### ENDPOINTS --------------------------------------------------------------------------------------------------------------------------------------------------------

# OBTENER TODOS LOS PRODUCTOS (findAll)
@router.get("/")
async def get_all_productos():
    return lista_productos


# OBTENER UN PRODUCTO POR ID (findById)
@router.get("/{id}")
async def get_producto(id: int):
    return find_by_id(id)


# CREAR UN NUEVO PRODUCTO (save)
@router.post("/", status_code=201)
async def create_producto(producto: Producto): 
    producto.id = max([p.id for p in lista_productos], default=0) + 1   # ESTO ASEGURA QUE EL ID NO COINCIDA CON NINGÚN OTRO
    if any(p.nombre == producto.nombre for p in lista_productos):
        raise HTTPException(status_code=409, detail="Ya existe un producto con el mismo nombre")
        # HE PUESTO 409 PORQUE HE VISTO POR INTERNET QUE SE PONE PARA ESTOS CASOS.
    else:
        lista_productos.append(producto)
        return producto


# EDITAR UN PRODUCTO POR ID (save / edit)
@router.put("/{id}", status_code=200)
async def update_producto(id: int, producto: Producto):
    producto_lista = find_by_id(id)
    producto_lista.nombre = producto.nombre
    producto_lista.precio = producto.precio
    producto_lista.en_oferta = producto.en_oferta
    return producto_lista


# BORRAR UN PRODUCTO POR ID (delete)
@router.delete("/{id}", status_code=204)
async def delete_producto(id: int):
    producto = find_by_id(id)
    lista_productos.remove(producto)


### MÉTODOS DE REPOSITORIO -------------------------------------------------------------------------------------------------------------------------------------------

def find_by_id(id: int):
    for producto in lista_productos:
        if producto.id == id:
            return producto
    raise HTTPException(status_code=404, detail=f"No se ha encontrado ningún producto con ID: {id}")
