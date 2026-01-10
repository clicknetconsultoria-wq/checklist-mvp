from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import uuid

from fastapi.responses import StreamingResponse
from app.services.pdf import gerar_pdf_layout_estatico

from app.database import get_db
from app.models import Checklist
from app.schemas import ChecklistCreate, ChecklistResponse
from app.services.laudo import gerar_laudo

from fastapi.responses import StreamingResponse
from app.services.pdf_teste import gerar_pdf_laudo

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
def formulario(request: Request):
    return templates.TemplateResponse("checklist.html", {"request": request})


@router.post("/checklists", response_model=ChecklistResponse)
def criar_checklist(payload: ChecklistCreate, db: Session = Depends(get_db)):
    checklist = Checklist(
        veiculo=payload.veiculo.dict(),
        itens=[item.dict() for item in payload.itens],
        observacoes=payload.observacoes,
        responsavel=payload.responsavel,
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

@router.get("/checklists/{checklist_id}/pdf")
def baixar_pdf(checklist_id: str, db: Session = Depends(get_db)):
    checklist = db.query(Checklist).filter(Checklist.id == checklist_id).first()
    if not checklist:
        raise HTTPException(status_code=404, detail="Checklist não encontrado")

    pdf = gerar_pdf_laudo(checklist)

    return StreamingResponse(
        pdf,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f"inline; filename=laudo_{checklist_id}.pdf"
        }
    )

@router.get("/pdf-preview")
def preview_pdf():
    pdf = gerar_pdf_layout_estatico()
    return StreamingResponse(
        pdf,
        media_type="application/pdf",
        headers={"Content-Disposition": "inline; filename=checklist.pdf"}
    )