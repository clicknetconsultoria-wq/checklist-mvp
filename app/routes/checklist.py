from fastapi import APIRouter, HTTPException
from app.schemas import ChecklistCreate
from app.services.whatsapp import enviar_checklist

router = APIRouter(
    prefix="/checklist",
    tags=["Checklist"]
)

@router.post("/send")
async def send_checklist(data: ChecklistCreate):
    try:
        await enviar_checklist(data.dict())
        return {"success": True}
    except Exception as e:
        print("❌ Erro envio WhatsApp:", e)
        raise HTTPException(
            status_code=500,
            detail="Falha ao enviar WhatsApp"
        )
