from fastapi import APIRouter, HTTPException
from app.schemas import ChecklistCreate
from app.services.whatsapp import enviar_checklist
from fastapi.responses import StreamingResponse
from app.services.pdf import gerar_pdf_layout_estatico

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

@router.get("/pdf-preview")
def preview_pdf():
    pdf = gerar_pdf_layout_estatico()
    return StreamingResponse(
        pdf,
        media_type="application/pdf",
        headers={
            "Content-Disposition": "inline; filename=checklist.pdf"
        }
    )