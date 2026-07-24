# hastyplot

> This library is completely generated from a marimo notebook.
>
> You can inspect the full implementation/docs/demo/test suite be clicking the button below.  

[![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/koaning/qplot/blob/main/qplot.py/wasm)

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
qplot(cars, "Origin", "Miles_per_Gallon", mark="boxplot")

# Matrix / heatmap from long-table data
qplot(matrix_df, "col", "row", mark="rect", color="value")

# Faceted scatter
qplot(cars, "Horsepower", "Miles_per_Gallon",
      facet_wrap="Cylinders", columns=3, width=200, height=150)

# Lines grouped without color
qplot(stocks, "date", "price", mark="line", group="symbol")

# Lines grouped with a fixed color
qplot(stocks, "date", "price", mark="line", group="symbol", color="#red")

# Histogram with custom bins
qplot(cars, "Horsepower", bins=20, theme="clean")

# Area chart
qplot(stocks, "date", "price", mark="area", color="symbol")

# Step chart
qplot(stocks, "date", "price", mark="step", color="symbol")

# With axis limits and tooltip
qplot(cars, "Horsepower", "Miles_per_Gallon",
      x_lim=(0, 250), y_lim=(None, 40),
      tooltip=["Name", "Origin"])

# Polynomial smooth
qplot(cars, "Horsepower", "Miles_per_Gallon", smooth="poly")
```

## Themes

Pass the `theme` parameter to change the look of any chart:

```python
qplot(df, "x", "y", theme="clean")
```

- **`"default"`** — Altair's built-in styling, no customization applied.
- **`"clean"`** — No gridlines, dark axis colors, `system-ui` fonts, bold title.
- **`"minimal"`** — Light gridlines, no axis domain lines, Libre Franklin / Helvetica Neue fonts, bottom-oriented legend, and a custom color palette.

## Annotations

`hastyplot` also ships an `annotate` helper. It returns a plain Altair layer you
`+` onto any chart. Because `hastyplot` patches Altair's `+`, an annotation
composed onto a `qplot` base inherits its theme automatically — nothing special
needed.

```python
from hastyplot import qplot, annotate

# Mark a moment in time: dashed rule + hoverable warning badge
qplot(stocks, "date", "price", mark="line") + annotate(
    "2008-10-01", note="financial crisis", label="crash"
)

# Call out a specific point (pass a y): the badge lands on the data coordinate
qplot(cars, "Horsepower", "Miles_per_Gallon") + annotate(
    250, 15, note="most powerful", label="outlier"
)
```

Two modes, chosen by whether `y` is given:

- `annotate(x)` — draws a dashed vertical rule at `x` and pins the info-circle to
  the top of the panel.
- `annotate(x, y)` — places the info-circle on the `(x, y)` data coordinate; the
  rule defaults off.

The Vega-Lite type of `x` (and `y`) is inferred — datetime/ISO-string → temporal,
number → quantitative, other string → nominal — so it works on time-series and
scatter charts alike.

**Parameters**
- `x` — the x value to annotate.
- `y` — optional y value. When given, the marker sits on the data point.
- `note` — text shown on hover.
- `label` — short text pinned next to the info-circle.
- `rule` — draw a dashed vertical line at `x`. Defaults to `True` when `y` is
  omitted, `False` when a point is given.
- `marker` — draw a hoverable info-circle (default `True`).
- `marker_size` — size of the info-circle glyph (default `700`).
- `label_size` — font size of the pinned `label` text (default `13`).
- `color` — default color for both the line and the marker.
- `line_color` / `marker_color` — override the rule / info-circle color
  (each falls back to `color`).

## `API`

`hastyplot` exposes two functions: `qplot` (below) and `annotate` (above). In
`qplot`, `data` is the first argument so you can use `df.pipe(qplot, "x", "y")`.
Here's all the input options:

**Data & axes**
- `data` — DataFrame to plot.
- `x` — column for the x-axis.
- `y` — column for the y-axis. Omit for a histogram.
- `x_lim` / `y_lim` — axis limits as `(min, max)` tuples. Use `None` for an open bound.
- `tooltip` — list of column names to show on hover.

**Aesthetics**
- `color` — column to map to color.
  Use `"#red"` for a fixed named color value, or `"#ff0000"` for a fixed hex color.
- `size` — column to map to point size.
- `opacity` — a fixed float (e.g. `0.5`) or a column name.
- `group` — column to group by *without* changing color.
  Useful for separate lines per group in a uniform color.

**Mark & smoothing**
- `mark` — options: `"scatter"`, `"circle"`, `"line"`, `"bar"`, `"boxplot"`, `"hist"`, `"area"`, `"step"`, `"rect"`.
- `smooth` — overlay a trend line: `"loess"`, `"linear"`, `"poly"`, `"log"`, `"exp"`, `"pow"`.
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
