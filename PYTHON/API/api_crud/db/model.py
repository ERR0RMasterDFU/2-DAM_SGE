from sqlalchemy import Column, Integer, String, Float, Boolean
from db.database import Base

class Producto_tabla(Base):
    __tablename__ = "producto"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String, unique=True, nullable=False)
    precio = Column(Float, nullable=False)
    en_oferta = Column(Boolean, default=False)
