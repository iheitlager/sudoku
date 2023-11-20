VIRTUALENV ?= ~/.virtualenv
default: clean test

all: $(TARGETS)

clean: ## Clean all build files
	-@echo y | pip uninstall sudoku
	@rm -rf $(DOCS)/_build
	@find . -name *.pyc -delete
	@rm -rf build sudoku.egg* dist

.PHONY: test dist help

test: ## Run all tests
	@ruff check .
	@pytest

dist: ## Create a distribution
	@python setup.py sdist --formats=gztar bdist_wheel

dev: ## Install this package for development
	@pip install -e .

dev_env: ## Install the dev env
	@python -m pip install flake8 pytest ruff
	@python -m pip install ipykernel

virtualenv: $(VIRTUALENV)/sudoku/bin/activate
	virtualenv $(VIRTUALENV)/sudoku

help: ## Shows help screen
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'
	@echo ""