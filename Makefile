.PHONY: help install install-dev test lint format clean build upload-test upload

help:  ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install:  ## Install the package
	pip install -e .

install-dev:  ## Install the package with development dependencies
	pip install -e ".[dev]"

test:  ## Run tests
	pytest --verbose --cov=hello_world --cov-report=term-missing

lint:  ## Run linting checks
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=88 --statistics

format:  ## Format code with black and isort
	black .
	isort .

format-check:  ## Check code formatting
	black --check --diff .
	isort --check-only --diff .

clean:  ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

build:  ## Build the package
	python -m build

upload-test:  ## Upload to TestPyPI
	twine upload --repository testpypi dist/*

upload:  ## Upload to PyPI
	twine upload dist/*

run-hello:  ## Run the hello-world command
	hello-world

run-hello-farewell:  ## Run the hello-world command with farewell
	hello-world --farewell "Developer"
