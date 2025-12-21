.PHONY: test

test:
	@echo "[INFO] Running tests with unittest"
	python -m unittest discover -s tests
	@echo "[INFO] All tests finished!"