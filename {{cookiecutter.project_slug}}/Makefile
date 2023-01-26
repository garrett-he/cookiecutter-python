.DEFAULT_GOAL := help

.PHONY: help
help: ## Show help information
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

.PHONY: deps
deps: ## Install dependencies and Git hooks
	poetry install
	poetry run pre-commit install

.PHONY: lint
lint: ## Code analyse and lint
	poetry run pylint src/ tests/

.PHONY: test
test: ## Test in current Python version
	poetry run pytest --cov=src --cov-report=term-missing

.PHONY: tox
tox: ## Run tox with multiple Python versions
	poetry run tox

.PHONY: build
build: ## Build project
	poetry build

{% if cookiecutter.with_pyinstaller == 'yes' %}
.PHONY: dist
dist: ## Bundle project with pyinstaller
	rm -rf build/ dist/
	{% if cookiecutter.with_cython == 'yes' %}
	poetry run python setup.py build_ext --build-lib build
	cp .\src\{{cookiecutter.project_package}}\__main__.py .\build\{{cookiecutter.project_package}}\
	{% endif %}
	poetry run pyinstaller {{cookiecutter.project_slug}}.spec
	{% if 'GPL' in cookiecutter.license_id %}
	cp {CHANGELOG.md,COPYING,README.md} dist/
	{% else %}
	cp {CHANGELOG.md,LICENSE,README.md} dist/
	{% endif %}
{% endif %}

.PHONY: publish
publish: build ## Build and publish to remote index
	poetry publish --build

.PHONY: codecov
codecov: ## Upload coverage.xml to codecov.com
	poetry run pytest --cov=src --cov-report=xml
	codecov

.PHONY: clean
clean: ## Clean up cache files
	rm -rf .pytest_cache/ .tox/ build/ dist/
	rm -f .coverage coverage.xml
