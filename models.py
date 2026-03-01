from sqlalchemy import Column, String, Integer
from database import Base

class ProdutoDB(Base):
    __tablename__ = "produtos"

    nome = Column(String, primary_key=True, index=True)
    quantidade = Column(Integer)