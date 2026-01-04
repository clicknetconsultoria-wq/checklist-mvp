import json
import uuid
from datetime import datetime
from pathlib import Path

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
    data = load_checklists()

    checklist = {
        "id": str(uuid.uuid4()),
        "criado_em": datetime.utcnow().isoformat(),
        **payload
    }

    data.append(checklist)
    save_checklists(data)

    return checklist


def get_checklist_by_id(checklist_id: str):
    data = load_checklists()

    for checklist in data:
        if checklist["id"] == checklist_id:
            return checklist

    return None
