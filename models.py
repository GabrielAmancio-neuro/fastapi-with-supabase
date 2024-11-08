from pydantic import BaseModel
from sqlmodel import Field

class Empresa(BaseModel):
    idempresa:  int = Field(None, title="Id da Empresa")
    nome: str = Field(None, title="Nome da Empresa")
