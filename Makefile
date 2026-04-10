build:
	uvx mobuild export qplot.py src/hastyplot

test:
	uvx --with marimo --with altair --with pandas --with vega-datasets pytest qplot.py

docs: build
	uvx --with wigglystuff --with altair python scripts/generate_docs.py

pypi: build
	uv build
	uv publish
