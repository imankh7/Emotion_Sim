
from src.data_prep.redact import redact_text

def test_redact_email():
    assert "[EMAIL]" in redact_text("contact me a@b.com")
