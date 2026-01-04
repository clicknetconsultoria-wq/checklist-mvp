import json
import uuid
from datetime import datetime
from pathlib import Path
from app.database import SessionLocal
from app.models_db import Checklist

DATA_FILE = Path("app/data/checklists.json")


def load_checklists():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_checklists(data):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)



def create_checklist(payload: dict):
    db = SessionLocal()
    checklist = Checklist(**payload)
    db.add(checklist)
    db.commit()
    db.refresh(checklist)
    db.close()
    return checklist


def get_checklist_by_id(checklist_id: str):
    db = SessionLocal()
    checklist = db.query(Checklist).filter(Checklist.id == checklist_id).first()
    db.close()
    return checklist


def list_checklists():
    db = SessionLocal()
    checklists = db.query(Checklist).all()
    db.close()
    return checklists
