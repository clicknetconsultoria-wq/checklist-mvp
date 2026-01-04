from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class VeiculoSchema(BaseModel):
    placa: str
    modelo: Optional[str] = None

class ItemChecklistSchema(BaseModel):
    descricao: str
    valor: str

class ChecklistCreate(BaseModel):
    veiculo: VeiculoSchema
    itens: List[ItemChecklistSchema]
    responsavel: str
    observacoes: Optional[str] = None

class ChecklistResponse(ChecklistCreate):
    id: str
    criado_em: datetime

    class Config:
        from_attributes = True
