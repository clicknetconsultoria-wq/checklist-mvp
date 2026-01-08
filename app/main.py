from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.database import Base, engine
from app.routes.checklist import router as checklist_router
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Checklist Veicular MVP",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(checklist_router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
def health():
    return JSONResponse({
        "status": "ok",
        "service": "Checklist MVP",
        "integration": "Railway → WhatsApp Bot"
    })