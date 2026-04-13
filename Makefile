install:
	uv venv --allow-existing
	uv pip install -e .

build:
	uvx marimo -y export session qplot.py
	uvx mobuild export qplot.py src/hastyplot/__init__.py

test:
	uvx --with marimo --with altair --with pandas --with vega-datasets pytest qplot.py
	uv run pytest tests

pypi: build test
	uv build
	uv publish
