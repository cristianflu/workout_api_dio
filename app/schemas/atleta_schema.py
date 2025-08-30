from pydantic import BaseModel

class AtletaBase(BaseModel):
    nome: str
    cpf: str
    categoria_id: int
    centro_id: int

class AtletaCreate(AtletaBase):
    pass

class AtletaOut(BaseModel):
    nome: str
    categoria_id: int
    centro_id: int

    class Config:
        orm_mode = True
