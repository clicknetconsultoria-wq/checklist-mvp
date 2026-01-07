from fastapi import APIRouter
from app.routes.checklist import router as checklist_router

router = APIRouter()
router.include_router(checklist_router)
