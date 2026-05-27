install:
	uv venv --allow-existing
	uv pip install -e .

.PHONY: install build test pypi clean

build:
	uvx marimo -y export session qplot.py
	uvx mobuild export qplot.py src/hastyplot/__init__.py

test:
	uvx --with marimo --with altair --with pandas --with vega-datasets pytest qplot.py
	uv run pytest tests

pypi: clean build test
	uv build
	uv publish

clean:
	rm -rf build dist src/hastyplot.egg-info
	find . -type d \( -name "__pycache__" -o -name ".pytest_cache" \) -prune -exec rm -rf {} +
