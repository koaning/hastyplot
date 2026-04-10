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

<!-- API_DOCS_START -->
## `hastyplot.qplot.qplot`

> function

```python
qplot(data, x: str, y: str | None = None, *, color: str | None = None, size: str | None = None, opacity: float | str = 0.7, group: str | None = None, geom: str = 'auto', smooth: str | None = None, bandwidth: float = 0.3, bins: int | None = None, facet_col: str | None = None, facet_row: str | None = None, facet_wrap: str | None = None, columns: int | None = None, width: int | None = None, height: int | None = None, title: str | None = None, subtitle: str | None = None, theme: str = 'default', actions: bool = False) -> altair.vegalite.v6.api.Chart
```

Quick plot for Altair. Inspired by ggplot2's qplot.

`data` is the first argument so you can use `df.pipe(qplot, "x", "y")`.

**Data & axes**
- `data` — DataFrame to plot.
- `x` — column for the x-axis.
- `y` — column for the y-axis. Omit for a histogram.

**Aesthetics**
- `color` — column to map to color.
- `size` — column to map to point size.
- `opacity` — a fixed float (e.g. `0.5`) or a column name.
- `group` — column to group by *without* changing color.
  Useful for separate lines per group in a uniform color.

**Geom & smoothing**
- `geom` — `"auto"` picks `"hist"` for x-only, `"scatter"` for x+y.
  Options: `"scatter"`, `"circle"`, `"line"`, `"bar"`, `"boxplot"`, `"hist"`.
- `smooth` — overlay a trend line: `"loess"`, `"linear"`, `"poly"`,
  `"log"`, `"exp"`, `"pow"`.
- `bandwidth` — loess bandwidth, 0 to 1 (default `0.3`). Lower = wigglier.
- `bins` — number of histogram bins. Omit for Altair's default.

**Faceting**
- `facet_col` / `facet_row` — column names for a facet grid.
- `facet_wrap` — single column, wraps into rows.
- `columns` — max columns before wrapping (default `3`).

**Layout & appearance**
- `width` / `height` — chart size in pixels (per panel when faceted).
- `title` / `subtitle` — chart title and subtitle.
- `theme` — `"default"`, `"clean"`, or `"minimal"`.
- `actions` — show the Vega-Lite export menu (default `False`).

| Name | Type | Default |
| --- | --- | --- |
| `data` |  |  |
| `x` | `str` |  |
| `y` | `str | None` | `None` |
| `color` | `str | None` | `None` |
| `size` | `str | None` | `None` |
| `opacity` | `float | str` | `0.7` |
| `group` | `str | None` | `None` |
| `geom` | `str` | `'auto'` |
| `smooth` | `str | None` | `None` |
| `bandwidth` | `float` | `0.3` |
| `bins` | `int | None` | `None` |
| `facet_col` | `str | None` | `None` |
| `facet_row` | `str | None` | `None` |
| `facet_wrap` | `str | None` | `None` |
| `columns` | `int | None` | `None` |
| `width` | `int | None` | `None` |
| `height` | `int | None` | `None` |
| `title` | `str | None` | `None` |
| `subtitle` | `str | None` | `None` |
| `theme` | `str` | `'default'` |
| `actions` | `bool` | `False` |
<!-- API_DOCS_END -->
