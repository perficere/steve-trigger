.PHONY: get-poetry
get-poetry:
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

.PHONY: createvenv
createvenv:
	python3 -m venv .venv
	poetry run pip3 install --upgrade pip
	poetry run poetry install

.PHONY: black
black:
	poetry run black . --check

.PHONY: black!
black!:
	poetry run black .

.PHONY: flake8
flake8:
	poetry run flake8 .

.PHONY: isort
isort:
	poetry run isort . --check

.PHONY: isort!
isort!:
	poetry run isort .

.PHONY: format!
format!: black! isort!
