VIRTUALENV ?= ~/.virtualenv
default: clean test

all: $(TARGETS)

clean: ## Clean all build files
	-@echo y | pip uninstall sudoku
	@rm -rf $(DOCS)/_build
	@rm -rf .coverage
	@find . -name *.pyc -delete
	@rm -rf build sudoku.egg* dist

.PHONY: test dist help coverage

test: ## Run all tests
	@ruff check .
	@pytest

coverage: ## Checks the coverage
	@coverage run -m pytest
	@coverage report -m 

dist: ## Create a distribution
	@python setup.py sdist --formats=gztar bdist_wheel

dev: ## Install this package for development
	@pip install -e .

dev_env: ## Install the dev env
	@python -m pip install flake8 ruff
	@python -m pip install pytest
	@python -m pip install coverage
	@python -m pip install ipykernel
	@python -m pip install -r requirements.txt

virtualenv: $(VIRTUALENV)/sudoku/bin/activate
	virtualenv $(VIRTUALENV)/sudoku

help: ## Shows help screen
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'
	@echo ""