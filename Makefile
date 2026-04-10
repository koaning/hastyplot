build:
    uvx marimo -y export session qplot.py
	uvx mobuild export qplot.py src/hastyplot

test:
	uvx --with marimo --with altair --with pandas --with vega-datasets pytest qplot.py

pypi: build test
	uv build
	uv publish
