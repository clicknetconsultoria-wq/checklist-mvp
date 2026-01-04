from pydantic import BaseModel
from datetime import datetime
from typing import Dict, Optional

class VeiculoSchema(BaseModel):
    placa: str
    modelo: Optional[str] = None

class ChecklistCreate(BaseModel):
    cliente: str
    tecnico: str
    veiculo: VeiculoSchema
    checklist: Dict[str, str]

class ChecklistResponse(ChecklistCreate):
    id: str
    criado_em: datetime

    class Config:
        from_attributes = True
