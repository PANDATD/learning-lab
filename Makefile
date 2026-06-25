.PHONY: check lint format fix test typecheck clean

lint:
	uv run ruff check .

format:
	uv run ruff format .

fix:
	uv run ruff check . --fix
	uv run ruff format .

typecheck:
	uv run mypy .

test:
	uv run pytest -v

check:
	uv run ruff check .
	uv run ruff format --check .
	uv run mypy .
	uv run pytest -v

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -name "*.pyc" -delete
