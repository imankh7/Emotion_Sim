
# Minimal placeholders. Real logic will be built in Colab & synced back.
from typing import List, Dict
from src.models.config import ModelConfig
from src.data_prep.redact import redact_text

CFG = ModelConfig()

def analyze_note(text: str, user_id: str | None = None) -> Dict:
    clean = redact_text(text)
    # TODO: load embedding model + emotion classifier from artifacts
    return {
        "redacted_text": clean,
        "emotions": {"anxiety": 0.42, "stress": 0.37, "sadness": 0.15},
        "risk_flags": {"self_harm": False},
    }

def similar_notes(text: str, user_id: str | None = None, k: int = 5) -> List[Dict]:
    # TODO: vectorize + query Chroma/pgvector index
    return [{"note_id": "demo-1", "score": 0.78, "preview": "Feeling restless before exams..."}]

def suggest_coping(text: str, user_id: str | None = None, k: int = 3) -> List[Dict]:
    # TODO: RAG over curated coping tips; return grounded, reference-linked snippets
    return [
        {"title": "Box Breathing (4-4-4-4)", "source": "kb/breathing.md"},
        {"title": "Sleep Hygiene Checklist", "source": "kb/sleep.md"},
        {"title": "Worry Time Technique", "source": "kb/cbt.md"},
    ]
