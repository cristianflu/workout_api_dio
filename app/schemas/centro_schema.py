from pydantic import BaseModel

class CentroBase(BaseModel):
    nome: str

class CentroCreate(CentroBase):
    pass

class CentroOut(CentroBase):
    class Config:
        orm_mode = True
