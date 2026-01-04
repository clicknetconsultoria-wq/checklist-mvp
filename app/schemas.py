from pydantic import BaseModel
from datetime import datetime
from typing import List

class VeiculoSchema(BaseModel):
    placa: str
    modelo: str

class ItemChecklistSchema(BaseModel):
    descricao: str
    valor: str

class ChecklistResponse(BaseModel):
    id: str
    veiculo: VeiculoSchema
    itens: List[ItemChecklistSchema]
    observacoes: str | None
    responsavel: str
    criado_em: datetime

    class Config:
        from_attributes = True  # 👈 SQLAlchemy
