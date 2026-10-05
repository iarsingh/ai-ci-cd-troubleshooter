PYTHON ?= python3
.PHONY: test run docker
test:
	$(PYTHON) -m pytest -q
run:
	PYTHONPATH=src $(PYTHON) -m uvicorn citrouble.main:app --reload --port 8080
docker:
	docker build -t ai-ci-cd-troubleshooter:local .
