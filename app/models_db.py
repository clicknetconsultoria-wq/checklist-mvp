from sqlalchemy import Column, String, DateTime, JSON
from datetime import datetime
from app.database import Base
import uuid

class Checklist(Base):
    __tablename__ = "checklists"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    veiculo = Column(JSON)
    itens = Column(JSON)
    observacoes = Column(String)
    responsavel = Column(String)
    criado_em = Column(DateTime, default=datetime.utcnow)
