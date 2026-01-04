from fastapi import APIRouter, HTTPException
from app.schemas import ChecklistResponse
from app.storage import create_checklist, get_checklist_by_id

router = APIRouter()


@router.post("/checklists", response_model=ChecklistResponse)
def criar_checklist(payload: dict):
    return create_checklist(payload)


@router.get("/checklists/{checklist_id}", response_model=ChecklistResponse)
def obter_checklist(checklist_id: str):
    checklist = get_checklist_by_id(checklist_id)

    if not checklist:
        raise HTTPException(status_code=404, detail="Checklist não encontrado")

    return checklist
