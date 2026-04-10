# hastyplot

> This library is completely generated from a marimo notebook.
>
> You can inspect the full implementation/docs/demo/test suite be clicking the button below.  

[![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/koaning/qplot/blob/main/qplot.py)

Hasty plotting for Altair, inspired by ggplot2's `qplot`.

```python
from hastyplot import qplot

# Scatter plot
qplot(df, "x", "y")

# Histogram (x-only)
qplot(df, "x")

# With pipe
df.pipe(qplot, "x", "y", color="group")
```

## Install

```bash
uv add hastyplot
```

## Examples

```python
# Scatter with color and smooth
qplot(cars, "Horsepower", "Miles_per_Gallon",
      color="Origin", smooth="loess",
      title="HP vs MPG", theme="minimal")

# Boxplot
qplot(cars, "Origin", "Miles_per_Gallon", geom="boxplot")

# Faceted scatter
qplot(cars, "Horsepower", "Miles_per_Gallon",
      facet_wrap="Cylinders", columns=3, width=200, height=150)

# Lines grouped without color
qplot(stocks, "date", "price", geom="line", group="symbol")

# Histogram with custom bins
qplot(cars, "Horsepower", bins=20, theme="clean")
```

