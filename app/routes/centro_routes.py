from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.config import SessionLocal
from app.models.centro_model import Centro
from app.schemas.centro_schema import CentroCreate, CentroOut
from sqlalchemy.exc import IntegrityError

router = APIRouter(prefix="/centros", tags=["Centros"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=CentroOut, status_code=201)
def criar_centro(centro: CentroCreate, db: Session = Depends(get_db)):
    novo = Centro(**centro.dict())
    db.add(novo)
    try:
        db.commit()
        db.refresh(novo)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=303, detail=f"Já existe um centro com o nome: {centro.nome}")
    return novo

@router.get("/", response_model=list[CentroOut])
def listar_centros(db: Session = Depends(get_db)):
    return db.query(Centro).all()
