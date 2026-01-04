from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.storage import create_checklist
from app.schemas import ChecklistCreate, ChecklistResponse, ChecklistListResponse
from app.storage import get_checklist_by_id
from app.services.laudo import gerar_laudo
from app.schemas import LaudoResponse
from app.storage import list_checklists



router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
def formulario(request: Request):
    return templates.TemplateResponse(
        "checklist.html", {"request": request}
    )


@router.post("/checklists", response_model=ChecklistResponse)
def criar_checklist(payload: ChecklistCreate):
    checklist = create_checklist(payload.dict())
    return checklist

@router.get("/checklists/{checklist_id}/laudo", response_model=LaudoResponse)
def obter_laudo(checklist_id: str):
    checklist = get_checklist_by_id(checklist_id)

    if not checklist:
        raise HTTPException(status_code=404, detail="Checklist não encontrado")

    laudo = gerar_laudo(checklist)

    return {
        "checklist_id": checklist_id,
        "laudo": laudo
    }


@router.get("/checklists", response_model=list[ChecklistResponse])
def listar_checklists(db: Session = Depends(get_db)):
    return db.query(Checklist).all()

