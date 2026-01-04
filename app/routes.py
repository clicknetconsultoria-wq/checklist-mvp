from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import uuid

from app.database import get_db
from app.models import Checklist
from app.schemas import ChecklistCreate, ChecklistResponse
from app.services.laudo import gerar_laudo

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
def formulario(request: Request):
    return templates.TemplateResponse("checklist.html", {"request": request})


@router.post("/checklists", response_model=ChecklistResponse)
def criar_checklist(payload: ChecklistCreate, db: Session = Depends(get_db)):
    checklist = Checklist(
        id=str(uuid.uuid4()),
        cliente=payload.cliente,
        tecnico=payload.tecnico,
        veiculo=payload.veiculo.dict(),
        checklist=payload.checklist,
    )
    db.add(checklist)
    db.commit()
    db.refresh(checklist)
    return checklist


@router.get("/checklists", response_model=list[ChecklistResponse])
def listar_checklists(db: Session = Depends(get_db)):
    return db.query(Checklist).all()


@router.get("/checklists/{checklist_id}", response_model=ChecklistResponse)
def obter_checklist(checklist_id: str, db: Session = Depends(get_db)):
    checklist = db.query(Checklist).filter(Checklist.id == checklist_id).first()
    if not checklist:
        raise HTTPException(status_code=404, detail="Checklist não encontrado")
    return checklist


@router.get("/checklists/{checklist_id}/laudo")
def obter_laudo(checklist_id: str, db: Session = Depends(get_db)):
    checklist = db.query(Checklist).filter(Checklist.id == checklist_id).first()
    if not checklist:
        raise HTTPException(status_code=404, detail="Checklist não encontrado")

    laudo = gerar_laudo(checklist)
    return {"checklist_id": checklist_id, "laudo": laudo}
