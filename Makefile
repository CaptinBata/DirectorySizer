.ONESHELL:
install:
	poetry install

.ONESHELL:
update:
	poetry update

local: install
	poetry run pre-commit install

.ONESHELL: #local
lint: flake8 black

.ONESHELL:
flake8: #local
	poetry run flake8

.ONESHELL:
black: #local
	poetry run black --diff --check .

.ONESHELL:
black-fix: #local
	poetry run black .

.ONESHELL:
bandit: #local
	poetry run bandit -r directory_sizer -q -n 3

.ONESHELL:
safety: #local
	poetry export -f requirements.txt -o requirements.txt
	poetry run safety check -r requirements.txt
	rm requirements.txt

.ONESHELL:
utest: #local
	PYTHONPATH=directory_sizer/ \
		poetry run pytest \
		--cov-report term:skip-covered \
		--cov-report html:coverage_report \
		--cov-report xml:coverage_report/coverage.xml \
		--cov=directory_sizer tests/unit_tests -ra -s

.ONESHELL:
test: utest

.ONESHELL:
test-vv: #local
	PYTHONPATH=directory_sizer/ \
		poetry run pytest -vv \

.ONESHELL:
pre-build:
	poetry export --without-hashes -f requirements.txt -o requirements.txt 
