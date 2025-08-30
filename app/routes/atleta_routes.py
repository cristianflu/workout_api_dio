from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from fastapi_pagination import Page, paginate
from app.core.config import SessionLocal
from app.models.atleta_model import Atleta
from app.schemas.atleta_schema import AtletaCreate, AtletaOut
from sqlalchemy.exc import IntegrityError

router = APIRouter(prefix="/atletas", tags=["Atletas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=AtletaOut, status_code=201)
def criar_atleta(atleta: AtletaCreate, db: Session = Depends(get_db)):
    novo = Atleta(**atleta.dict())
    db.add(novo)
    try:
        db.commit()
        db.refresh(novo)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=303, detail=f"Já existe um atleta cadastrado com o cpf: {atleta.cpf}")
    return novo

@router.get("/", response_model=Page[AtletaOut])
def listar_atletas(nome: str = Query(None), cpf: str = Query(None), db: Session = Depends(get_db)):
    query = db.query(Atleta)
    if nome:
        query = query.filter(Atleta.nome.ilike(f"%{nome}%"))
    if cpf:
        query = query.filter(Atleta.cpf == cpf)
    return paginate(query.all())
