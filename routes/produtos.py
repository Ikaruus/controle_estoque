from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import ProdutoDB
from schemas import Produto

router = APIRouter()

@router.get("/produtos")
def listar_produtos():
    db: Session = SessionLocal()
    produtos = db.query(ProdutoDB).all()
    db.close()
    return produtos

@router.post("/produtos")
def adicionar_produto(produto: Produto):
    db: Session = SessionLocal()

    produto_existente = db.query(ProdutoDB).filter(
        ProdutoDB.nome == produto.nome
    ).first()

    if produto_existente:
        db.close()
        raise HTTPException(status_code=400, detail="Produto já existe")

    novo_produto = ProdutoDB(
        nome=produto.nome,
        quantidade=produto.quantidade
    )

    db.add(novo_produto)
    db.commit()
    db.close()

    return {"mensagem": "Produto adicionado com sucesso!"}

@router.delete("/produtos/{nome}")
def remover_produto(nome: str):
    db: Session = SessionLocal()

    produto = db.query(ProdutoDB).filter(
        ProdutoDB.nome == nome
    ).first()

    if not produto:
        db.close()
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    db.delete(produto)
    db.commit()
    db.close()

    return {"mensagem": "Produto removido com sucesso!"}