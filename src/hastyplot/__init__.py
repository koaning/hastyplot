__all__ = ['qplot']


import altair as alt

def _clean_label(name):
    """Lowercase and replace -/_ with spaces."""
    return name.replace("_", " ").replace("-", " ").lower()


def qplot(
    data,
    x: str,
    y: str | None = None,
    *,
    # Aesthetics
    color: str | None = None,
    size: str | None = None,
    opacity: float | str = 0.7,
    group: str | None = None,
    # Geom & smoothing
    geom: str = "auto",
    smooth: str | None = None,
    bandwidth: float = 0.3,
    bins: int | None = None,
    # Faceting
    facet_col: str | None = None,
    facet_row: str | None = None,
    facet_wrap: str | None = None,
    columns: int | None = None,
    # Layout & appearance
    width: int | None = None,
    height: int | None = None,
    title: str | None = None,
    subtitle: str | None = None,
    theme: str = "default",
    actions: bool = False,
) -> alt.Chart:
    """Quick plot for Altair. Inspired by ggplot2's qplot.

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
    """
    chart = alt.Chart(data)

    # Auto-select geom
    if geom == "auto":
        geom = "hist" if y is None else "scatter"

    # Clean axis labels
    x_enc = (
        alt.X(x, bin=alt.Bin(maxbins=bins) if bins is not None else True, title=_clean_label(x))
        if geom == "hist"
        else alt.X(x, title=_clean_label(x))
    )
    y_enc = (
        alt.Y("count()", title="count")
        if geom == "hist"
        else (alt.Y(y, title=_clean_label(y)) if y else None)
    )

    # Build the mark + encoding
    if geom == "scatter":
        chart = chart.mark_point(
            filled=True, opacity=opacity if isinstance(opacity, (int, float)) else 0.7
        ).encode(x=x_enc, y=y_enc)
    elif geom == "circle":
        chart = chart.mark_circle(
            opacity=opacity if isinstance(opacity, (int, float)) else 0.7
        ).encode(x=x_enc, y=y_enc)
    elif geom == "hist":
        chart = chart.mark_bar().encode(x=x_enc, y=y_enc)
    elif geom == "line":
        chart = chart.mark_line(strokeWidth=2).encode(x=x_enc, y=y_enc)
    elif geom == "bar":
        chart = chart.mark_bar().encode(x=x_enc, y=y_enc)
    elif geom == "boxplot":
        chart = chart.mark_boxplot().encode(x=x_enc, y=y_enc)
    else:
        raise ValueError(f"Unknown geom: {geom}")

    # Group: splits data by a column (separate marks) but no color distinction
    if group is not None:
        chart = chart.encode(detail=alt.Detail(group))

    # Optional encodings
    if color is not None:
        chart = chart.encode(color=alt.Color(color, title=_clean_label(color)))
    if size is not None:
        chart = chart.encode(size=alt.Size(size, title=_clean_label(size)))
    if isinstance(opacity, str):
        chart = chart.encode(opacity=alt.Opacity(opacity, title=_clean_label(opacity)))

    # Smooth: overlay a trend line
    if smooth is not None and y is not None:
        smooth_base = alt.Chart(data)
        groupby = [color] if color is not None else []
        if smooth == "loess":
            trend = (
                smooth_base.transform_loess(x, y, groupby=groupby, bandwidth=bandwidth)
                .mark_line(strokeWidth=3, opacity=0.9)
                .encode(x=alt.X(x, title=_clean_label(x)), y=alt.Y(y, title=_clean_label(y)))
            )
        else:
            trend = (
                smooth_base.transform_regression(x, y, method=smooth, groupby=groupby)
                .mark_line(strokeWidth=3, opacity=0.9)
                .encode(x=alt.X(x, title=_clean_label(x)), y=alt.Y(y, title=_clean_label(y)))
            )
        if color is not None:
            trend = trend.encode(color=alt.Color(color, title=_clean_label(color)))
        chart = chart + trend

    # Width and height (applied per facet panel or to whole chart)
    if width is not None or height is not None:
        props = {}
        if width is not None:
            props["width"] = width
        if height is not None:
            props["height"] = height
        chart = chart.properties(**props)

    # Faceting
    if facet_wrap is not None:
        chart = chart.facet(
            alt.Facet(facet_wrap, title=_clean_label(facet_wrap)),
            columns=columns or 3,
        )
    elif facet_col is not None and facet_row is not None:
        chart = chart.facet(
            column=alt.Column(facet_col, title=_clean_label(facet_col)),
            row=alt.Row(facet_row, title=_clean_label(facet_row)),
        )
    elif facet_col is not None:
        chart = chart.facet(column=alt.Column(facet_col, title=_clean_label(facet_col)))
    elif facet_row is not None:
        chart = chart.facet(row=alt.Row(facet_row, title=_clean_label(facet_row)))

    # Title + subtitle
    if title is not None:
        title_obj = alt.TitleParams(text=title, subtitle=subtitle or "")
        chart = chart.properties(title=title_obj)
    elif subtitle is not None:
        title_obj = alt.TitleParams(text="", subtitle=subtitle)
        chart = chart.properties(title=title_obj)

    # Embed options to control action menu
    chart = chart.properties(usermeta={"embedOptions": {"actions": actions}})

    # Apply theme
    chart = _apply_theme(chart, theme)

    return chart


_TITLE_COMMON = dict(anchor="start", offset=10, dx=40)


def _apply_theme(chart, theme):
    if theme == "default":
        return chart
    elif theme == "clean":
        return (
            chart.configure_axis(
                grid=False,
                domainColor="#333",
                tickColor="#333",
                labelFontSize=11,
                titleFontSize=12,
                titleFont="system-ui",
                labelFont="system-ui",
                labelColor="#555",
                titleColor="#333",
            )
            .configure_view(strokeWidth=0)
            .configure_title(
                fontSize=18,
                fontWeight="bold",
                font="system-ui",
                subtitleFont="system-ui",
                subtitleFontSize=13,
                subtitleColor="#666",
                color="#1a1a1a",
                **_TITLE_COMMON,
            )
            .configure_legend(
                labelFont="system-ui",
                titleFont="system-ui",
                labelFontSize=11,
                titleFontSize=11,
                symbolSize=80,
            )
        )
    elif theme == "minimal":
        return (
            chart.configure_axis(
                grid=True,
                gridColor="#e5e5e5",
                gridWidth=0.5,
                domain=False,
                tickSize=0,
                labelFontSize=11,
                titleFontSize=11,
                titleFont="'Libre Franklin', 'Helvetica Neue', sans-serif",
                labelFont="'Libre Franklin', 'Helvetica Neue', sans-serif",
                labelColor="#666",
                titleColor="#666",
                titleFontWeight="normal",
                labelPadding=8,
            )
            .configure_view(strokeWidth=0)
            .configure_title(
                fontSize=20,
                fontWeight=700,
                font="'Libre Franklin', 'Helvetica Neue', sans-serif",
                color="#1a1a1a",
                subtitleFont="'Libre Franklin', 'Helvetica Neue', sans-serif",
                subtitleFontSize=14,
                subtitleColor="#888",
                subtitleFontWeight="normal",
                subtitlePadding=4,
                **_TITLE_COMMON,
            )
            .configure_legend(
                labelFont="'Libre Franklin', 'Helvetica Neue', sans-serif",
                titleFont="'Libre Franklin', 'Helvetica Neue', sans-serif",
                labelFontSize=11,
                titleFontSize=11,
                titleFontWeight="normal",
                symbolSize=80,
                orient="bottom",
            )
            .configure_range(
                category=[
                    "#e15759",
                    "#4e79a7",
                    "#f28e2b",
                    "#76b7b2",
                    "#59a14f",
                    "#edc948",
                    "#b07aa1",
                    "#ff9da7",
                    "#9c755f",
                    "#bab0ac",
                ]
            )
        )
    else:
        raise ValueError(f"Unknown theme: {theme}")
