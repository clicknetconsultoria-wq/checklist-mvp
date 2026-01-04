from sqlalchemy import Column, String, DateTime, JSON
from datetime import datetime
from app.database import Base

class Checklist(Base):
    __tablename__ = "checklists"

    id = Column(String, primary_key=True, index=True)
    cliente = Column(String)
    tecnico = Column(String)
    veiculo = Column(JSON)
    checklist = Column(JSON)
    criado_em = Column(DateTime, default=datetime.utcnow)
