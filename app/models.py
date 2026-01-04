from pydantic import BaseModel
from typing import Dict, Optional

class Veiculo(BaseModel):
    placa: str
    modelo: Optional[str] = None

class ChecklistRequest(BaseModel):
    cliente: str
    tecnico: str
    veiculo: Veiculo
    checklist: Dict[str, str]
