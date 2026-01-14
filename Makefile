.PHONY: test install

test:
	@echo "[INFO] Running tests with unittest"
	python -m unittest discover -s tests
	@echo "[INFO] All tests finished!"

install:
	@echo "[INFO] Setting up virtual environment"
	@python3 -m venv .venv
	@echo "[INFO] Installing dependencies"
	@.venv/bin/pip install -r requirements.txt
	@echo "[INFO] Dependencies installed!"