from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.storage import create_checklist
from app.schemas import ChecklistCreate, ChecklistResponse

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
