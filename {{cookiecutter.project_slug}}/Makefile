.PHONY: install format lint test clean

install:
	poetry install

format:
	poetry run ruff format .
	poetry run ruff check --fix .

lint:
	poetry run ruff check .
	poetry run pyright

test:
	poetry run pytest tests/ --cov={{cookiecutter.project_slug}} --cov-report=term-missing

clean:
	rm -rf .coverage
	rm -rf htmlcov
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	rm -rf dist
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
