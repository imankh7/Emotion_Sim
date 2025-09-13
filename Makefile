
.PHONY: format lint test run

format:
	python -m black src tests

lint:
	python -m ruff src tests

test:
	pytest -q

run:
	uvicorn src.app.main:app --reload --port 8000
