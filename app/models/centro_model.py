from sqlalchemy import Column, Integer, String
from app.core.config import Base

class Centro(Base):
    __tablename__ = "centros"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True)
