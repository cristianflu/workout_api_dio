from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.config import SessionLocal
from app.models.categoria_model import Categoria
from app.schemas.categoria_schema import CategoriaCreate, CategoriaOut
from sqlalchemy.exc import IntegrityError

router = APIRouter(prefix="/categorias", tags=["Categorias"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=CategoriaOut, status_code=201)
def criar_categoria(categoria: CategoriaCreate, db: Session = Depends(get_db)):
    novo = Categoria(**categoria.dict())
    db.add(novo)
    try:
        db.commit()
        db.refresh(novo)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=303, detail=f"Já existe uma categoria com o nome: {categoria.nome}")
    return novo

@router.get("/", response_model=list[CategoriaOut])
def listar_categorias(db: Session = Depends(get_db)):
    return db.query(Categoria).all()
