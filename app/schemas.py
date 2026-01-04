from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime



class ChecklistItem(BaseModel):
    descricao: str
    valor: str


class Veiculo(BaseModel):
    placa: str
    modelo: Optional[str] = None


class ChecklistCreate(BaseModel):
    veiculo: Veiculo
    itens: List[ChecklistItem]
    observacoes: Optional[str] = None
    responsavel: str


class ChecklistResponse(ChecklistCreate):
    id: str
    criado_em: datetime

class LaudoResponse(BaseModel):
    checklist_id: str
    laudo: str