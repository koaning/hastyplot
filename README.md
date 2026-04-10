# hastyplot

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

## Features

- **Auto geom selection** -- x-only gives a histogram, x+y gives a scatter.
- **Geoms** -- `"scatter"`, `"circle"`, `"line"`, `"bar"`, `"boxplot"`, `"hist"`.
- **Aesthetics** -- `color`, `size`, `opacity`, `group`.
- **Smoothing** -- `smooth="loess"` overlays a trend line. Also supports `"linear"`, `"poly"`, `"log"`, `"exp"`, `"pow"`. Control loess wiggliness with `bandwidth`.
- **Faceting** -- `facet_col`, `facet_row` for grids. `facet_wrap` with `columns` for wrapped layouts.
- **Themes** -- `"default"`, `"clean"`, `"minimal"` (data journalism style).
- **Pipe-friendly** -- `data` is the first argument.

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
