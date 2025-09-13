
from fastapi import FastAPI
from pydantic import BaseModel
from src.rag.pipeline import analyze_note, similar_notes, suggest_coping

app = FastAPI(title="Emotion-Aware Note Understanding (Prototype)")

class NoteIn(BaseModel):
    user_id: str | None = None
    text: str

@app.post("/analyze_note")
def analyze(note: NoteIn):
    return analyze_note(note.text, user_id=note.user_id)

@app.post("/similar_notes")
def similar(note: NoteIn):
    return {"results": similar_notes(note.text, user_id=note.user_id, k=5)}

@app.post("/suggest_coping")
def coping(note: NoteIn):
    return {"suggestions": suggest_coping(note.text, user_id=note.user_id, k=3)}
