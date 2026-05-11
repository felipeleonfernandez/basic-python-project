.PHONY: help install dev-install test lint format type-check coverage clean

help:
	@echo "Available commands:"
	@echo "  make install       - Install the project"
	@echo "  make dev-install   - Install with development dependencies"
	@echo "  make test          - Run tests"
	@echo "  make test-cov      - Run tests with coverage report"
	@echo "  make lint          - Run linting checks"
	@echo "  make format        - Format code with black and isort"
	@echo "  make type-check    - Check types with mypy"
	@echo "  make clean         - Remove build artifacts and cache files"
	@echo "  make all           - Format, lint, type-check, and test"

install:
	pip install -e .

dev-install:
	pip install -e ".[dev]"

test:
	pytest

test-cov:
	pytest --cov=src/basic_python_project --cov-report=html --cov-report=term-missing

lint:
	flake8 src/ tests/

format:
	black src/ tests/
	isort src/ tests/

type-check:
	mypy src/

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -rf build/ dist/ *.egg-info/ htmlcov/ .coverage .mypy_cache/ .pytest_cache/

all: format lint type-check test
	@echo "All checks passed!"
