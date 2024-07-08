run:
	@uvicorn store.main:app --reload

precommit-install:
	@poetry run pre-commit install

test:
	@poetry run pytest

test-m:
	@poetry run pytest -s -rx -k $(K) --pdb store ./tests/
