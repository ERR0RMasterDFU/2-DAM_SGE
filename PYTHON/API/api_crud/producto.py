from producto import Producto
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# INICIA EL SERVIDOR: uvicorn producto:app --reload


class Producto(BaseModel):
    id: int
    nombre: str
    precio: float
    en_oferta: bool


lista_productos = [
    Producto(id=1, nombre="Sopa de tomate", en_oferta=True),
    Producto(id=2, nombre="Botella de agua", en_oferta=False),
    Producto(id=3, nombre="Pasta carbonara", en_oferta=True),
    Producto(id=4, nombre="Cereales de avena", en_oferta=False),
    Producto(id=5, nombre="Galletas de chocolate", en_oferta=True),
    Producto(id=6, nombre="Zuma de naranja", en_oferta=False),
    Producto(id=7, nombre="Pan integral", en_oferta=True),
    Producto(id=8, nombre="Arroz basmati", en_oferta=False),
    Producto(id=9, nombre="Croquetas", en_oferta=True),
    Producto(id=10, nombre="Queso cheddar", en_oferta=False),
    Producto(id=11, nombre="Mermelada de fresa", en_oferta=True),
    Producto(id=12, nombre="Yogur natural", en_oferta=False),
    Producto(id=13, nombre="Aceite de oliva", en_oferta=True),
    Producto(id=14, nombre="Chocolate negro", en_oferta=False),
    Producto(id=15, nombre="Café en grano", en_oferta=True),
    Producto(id=16, nombre="Té verde", en_oferta=False),
    Producto(id=17, nombre="Garbanzos enlatados", en_oferta=True),
    Producto(id=18, nombre="Harina de trigo", en_oferta=False),
    Producto(id=19, nombre="Miel", en_oferta=True),
    Producto(id=20, nombre="Sal marina", en_oferta=False),
]


@app.get("/")
async def get_all_productos():
    return lista_productos


@app.get("/{id}")
async def get_producto(id: int):
    return find_by_id(id)


@app.post("/", status_code=201)
async def create_producto(producto: Producto): 
    producto.id = max([p.id for p in lista_productos], default=0) + 1   # ESTO ASEGURA QUE EL ID NO COINCIDA CON NINGÚN OTRO
    if any(p.nombre == producto.nombre for p in lista_productos):
        raise HTTPException(status_code=409, detail="Ya existe un producto con el mismo nombre")
        # HE PUESTO 409 PORQUE HE VISTO POR INTERNET QUE SE PONE PARA ESTOS CASOS.
    else:
        lista_productos.append(producto)
        return producto


@app.put("/{id}", status_code=200)
async def update_producto(id: int, producto: Producto):
    producto_lista = find_by_id(id)
    producto_lista.nombre = producto.nombre
    producto_lista.precio = producto.precio
    producto_lista.en_oferta = producto.en_oferta
    return producto_lista


@app.delete("/{id}", status_code=204)
async def delete_producto(id: int):
    producto = find_by_id(id)
    lista_productos.remove(producto)


# MÉTODOS DE REPOSITORIO ------------------------------------------------------------------------------
       
def find_by_id(id: int):
    for producto in lista_productos:
        if producto.id == id:
            return producto
        raise HTTPException(status_code=404, detail=f"No se ha encontrado ningún producto con ID: {id}")











