from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Producto(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def get_all_productos():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def get_producto(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_producto(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}