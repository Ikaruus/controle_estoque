from pydantic import BaseModel

class Produto(BaseModel):
    nome: str
    quantidade: int

    class Config:
        orm_mode = True