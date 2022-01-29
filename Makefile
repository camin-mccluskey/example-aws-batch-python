.PHONY: install test lint

install:
	python -m pip install -r requirements.txt

run:
	python -m src.main

