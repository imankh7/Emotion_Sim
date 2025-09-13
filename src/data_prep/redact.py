
import re

# Very light redaction helpers (prototype-only; not production-ready).
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
PHONE = re.compile(r"\b\+?\d[\d\s().-]{7,}\b")

def redact_text(text: str) -> str:
    text = EMAIL.sub("[EMAIL]", text)
    text = PHONE.sub("[PHONE]", text)
    return text
