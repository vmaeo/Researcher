from datetime import datetime
import re
from pathlib import Path
import json

SESSION_DIR = Path("data/sessions")

def create_session(query):
    current_time = datetime.now().strftime("%Y-%m-%d")
    query_slug = query.lower().replace(" ", "-")
    query_fin = re.sub(r'[^a-z0-9-]', '', query_slug)
    session_id = f"{current_time}_{query_fin[:30]}"
    return {
        "session_id": session_id,
        "query": query,
        "notes": [],
        "sources": [],
        "summary": None,
        "created_at": current_time
    }

def save_session(session):
    SESSION_DIR.mkdir(parents=True, exist_ok=True)
    file_path = SESSION_DIR/f"{session['session_id']}.json"
    with open(file_path, "w") as f:
        json.dump(session, f, indent=2)
    
def load_session(session_id):
    file_path = SESSION_DIR/f"{session_id}.json"
    with open(file_path, "r") as f:
        return json.load(f)
    
def list_sessions():
    files = SESSION_DIR.glob("*.json")
    sessions = []
    for file_path in files:
        with open(file_path, "r") as f:
            sessions.append(json.load(f))
    return sessions