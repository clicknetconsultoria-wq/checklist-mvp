from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.database import Base, engine
from app.routes.checklist import router as checklist_router

app.include_router(checklist_router)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Checklist Veicular MVP",
    version="1.0.0"
)

#app.include_router(router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
