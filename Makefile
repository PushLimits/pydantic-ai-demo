VENV_DIR := .venv

.PHONY: all install format lint venv clean

all: install format lint

venv:
	uv venv $(VENV_DIR)

install: venv
	@. $(VENV_DIR)/bin/activate; \
	uv pip install -e ".[dev]"

format:
	ruff format .
	ruff check . --fix

lint:
	ruff format . --check
	ruff check .

clean:
	rm -rf $(VENV_DIR)