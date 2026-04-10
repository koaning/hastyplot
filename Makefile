build:
	uv run mobuild export qplot.py src/hastyplot

test:
	uvx --with marimo --with altair --with pandas --with vega-datasets pytest qplot.py

pypi: build
	uv build
	uv publish
