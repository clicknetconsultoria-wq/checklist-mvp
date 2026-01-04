from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.database import Base, engine
from app.routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Checklist Veicular MVP",
    version="1.0.0"
)

app.include_router(router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
