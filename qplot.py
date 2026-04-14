# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "altair>=5",
#     "pandas",
#     "vega-datasets",
#     "wigglystuff>=0.3.2",
#     "pytest==9.0.3",
# ]
# ///

import marimo

__generated_with = "0.23.1"
app = marimo.App(width="columns")


@app.cell(column=0, hide_code=True)
def _(mo):
    mo.md(r"""
    # `from hastyplot import qplot`

    This notebook contains the full definition of `qplot` from the `hastyplot` library. It's a quick plotting function for Altair,
    inspired by ggplot2's `qplot`. It is also a library that is fully developed in [marimo](https://marimo.io/gallery).

    ## The Setup

    Cells marked with `## EXPORT` are extracted into a Python package via
    [mobuild](https://github.com/koaning/mobuild).
    """)
    return


@app.cell
def _():
    ## EXPORT

    import altair as alt

    return (alt,)


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    from vega_datasets import data as vega_data

    return mo, pd, vega_data


@app.cell
def _(vega_data):
    # Load sample datasets
    cars = vega_data.cars()
    stocks = vega_data.stocks()
    return cars, stocks


@app.cell
def _(mo):
    theme_dropdown = mo.ui.dropdown(
        options=["default", "clean", "minimal"], value="minimal", label="Theme"
    )
    theme_dropdown
    return (theme_dropdown,)


@app.cell(hide_code=True)
def _(cars, mo, qplot, theme_dropdown):
    mo.hstack(
        [
            qplot(
                cars,
                "Horsepower",
                "Miles_per_Gallon",
                color="Origin",
                title="HP vs MPG",
                subtitle="With loess smooth per group",
                theme=theme_dropdown.value,
                smooth="loess",
            ),
            qplot(
                cars, "Origin", "Miles_per_Gallon", mark="boxplot", title="MPG by Origin", theme=theme_dropdown.value
            ),
            qplot(cars, "Horsepower", title="Distribution of Horsepower", theme=theme_dropdown.value),
        ],
        widths="equal",
    )
    return


@app.cell
def _(theme_dropdown):
    theme_dropdown
    return


@app.cell
def _(cars, qplot, theme_dropdown):
    qplot(
        cars,
        x="Horsepower",
        y="Miles_per_Gallon",
        mark="circle",
        color="Origin",
        facet_col="Origin",
        title="facet_col",
        subtitle="Notice how we can split here?",
        width=150,
        height=150,
        theme=theme_dropdown.value,
    )
    return


@app.cell
def _(theme_dropdown):
    theme_dropdown
    return


@app.cell
def _(cars, qplot, theme_dropdown):
    qplot(
        cars,
        "Horsepower",
        "Miles_per_Gallon",
        mark="circle",
        facet_wrap="Cylinders",
        columns=3,
        title="facet_wrap",
        width=150,
        height=150,
        theme=theme_dropdown.value,
    )
    return


@app.cell
def _(theme_dropdown):
    theme_dropdown
    return


@app.cell
def _(cars, mo, qplot, theme_dropdown):
    mo.hstack(
        [
            qplot(
                cars,
                "Horsepower",
                "Miles_per_Gallon",
                x_lim=(0, 250),
                y_lim=(None, 40),
                title="With axis limits",
                subtitle="x_lim=(0, 250), y_lim=(None, 40)",
                theme=theme_dropdown.value,
            ),
            qplot(
                cars,
                "Horsepower",
                "Miles_per_Gallon",
                title="Without axis limits",
                theme=theme_dropdown.value,
            ),
        ],
        widths="equal",
    )
    return


@app.cell
def _(cars, mo, qplot, stocks, theme_dropdown):
    mo.hstack(
        [
            qplot(
                stocks,
                "date",
                "price",
                mark="area",
                color="symbol",
                title="Area",
                theme=theme_dropdown.value,
            ),
            qplot(
                stocks,
                "date",
                "price",
                mark="step",
                color="symbol",
                title="Step",
                theme=theme_dropdown.value,
            ),
            qplot(
                cars,
                "Horsepower",
                "Miles_per_Gallon",
                tooltip=["Name", "Origin"],
                title="Tooltip",
                subtitle="Hover to see name and origin",
                theme=theme_dropdown.value,
            ),
        ],
        widths="equal",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    All the marimo tricks also still work, because it is *just* an altair chart that comes out.
    """)
    return


@app.cell
def _(theme_dropdown):
    theme_dropdown
    return


@app.cell
def _(cars, mo, qplot, theme_dropdown):
    _chart = qplot(
        cars,
        "Horsepower",
        "Miles_per_Gallon",
        color="Origin",
        title="HP vs MPG",
        subtitle="With loess smooth per group",
        theme=theme_dropdown.value,
        smooth="loess",
    )

    chart = mo.ui.altair_chart(_chart)
    chart
    return (chart,)


@app.cell
def _(chart):
    chart.value
    return


@app.cell(column=1, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Documentation

    This notebook also serves as documentation. We use a widget from wigglystuff to show all you need to know about the `qplot` function.
    """)
    return


@app.cell
def _(qplot):
    from wigglystuff import ApiDoc

    ApiDoc(qplot)
    return


@app.cell
def _():
    return


@app.cell(column=2, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Implementation

    This is where all the library code is implemented.
    """)
    return


@app.cell
def _(alt):
    ## EXPORT


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
        tooltip: list[str] | None = None,
        # Mark & smoothing
        mark: str = "auto",
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
        x_lim: tuple[float | None, float | None] | None = None,
        y_lim: tuple[float | None, float | None] | None = None,
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
        - `tooltip` — list of column names to show on hover (e.g. `["col_a", "col_b"]`).

        **Mark & smoothing**
        - `mark` — `"auto"` picks `"hist"` for x-only, `"scatter"` for x+y.
          Options: `"scatter"`, `"circle"`, `"line"`, `"area"`, `"step"`, `"bar"`, `"boxplot"`, `"hist"`.
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
        - `x_lim` / `y_lim` — tuple of (min, max) to set axis limits.
          Either side can be `None` to keep it automatic, e.g. `(None, 100)`.
        - `title` / `subtitle` — chart title and subtitle.
        - `theme` — `"default"`, `"clean"`, or `"minimal"`.
        - `actions` — show the Vega-Lite export menu (default `False`).
        """
        chart = alt.Chart(data)

        # Auto-select mark
        if mark == "auto":
            mark = "hist" if y is None else "scatter"

        # Axis limits & clipping
        x_scale = alt.Scale(domain=list(x_lim)) if x_lim is not None else alt.Undefined
        y_scale = alt.Scale(domain=list(y_lim)) if y_lim is not None else alt.Undefined
        _clip = x_lim is not None or y_lim is not None
        x_enc = (
            alt.X(x, bin=alt.Bin(maxbins=bins) if bins is not None else True, title=_clean_label(x), scale=x_scale)
            if mark == "hist"
            else alt.X(x, title=_clean_label(x), scale=x_scale)
        )
        y_enc = (
            alt.Y("count()", title="count", scale=y_scale)
            if mark == "hist"
            else (alt.Y(y, title=_clean_label(y), scale=y_scale) if y else None)
        )

        # Build the mark + encoding
        if mark == "scatter":
            chart = chart.mark_point(
                filled=True, opacity=opacity if isinstance(opacity, (int, float)) else 0.7, clip=_clip
            ).encode(x=x_enc, y=y_enc)
        elif mark == "circle":
            chart = chart.mark_circle(
                opacity=opacity if isinstance(opacity, (int, float)) else 0.7, clip=_clip
            ).encode(x=x_enc, y=y_enc)
        elif mark == "hist":
            chart = chart.mark_bar(clip=_clip).encode(x=x_enc, y=y_enc)
        elif mark == "line":
            chart = chart.mark_line(strokeWidth=2, clip=_clip).encode(x=x_enc, y=y_enc)
        elif mark == "bar":
            chart = chart.mark_bar(clip=_clip).encode(x=x_enc, y=y_enc)
        elif mark == "area":
            chart = chart.mark_area(
                opacity=opacity if isinstance(opacity, (int, float)) else 0.7, clip=_clip
            ).encode(x=x_enc, y=y_enc)
        elif mark == "step":
            chart = chart.mark_line(interpolate="step", strokeWidth=2, clip=_clip).encode(x=x_enc, y=y_enc)
        elif mark == "boxplot":
            chart = chart.mark_boxplot(clip=_clip).encode(x=x_enc, y=y_enc)
        else:
            raise ValueError(f"Unknown mark: {mark}")

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
        if tooltip is not None:
            chart = chart.encode(
                tooltip=[alt.Tooltip(col, title=_clean_label(col)) for col in tooltip]
            )

        # Smooth: overlay a trend line
        if smooth is not None and y is not None:
            smooth_base = alt.Chart(data)
            groupby = [color] if color is not None else []
            if smooth == "loess":
                trend = (
                    smooth_base.transform_loess(x, y, groupby=groupby, bandwidth=bandwidth)
                    .mark_line(strokeWidth=3, opacity=0.9, clip=_clip)
                    .encode(x=alt.X(x, title=_clean_label(x), scale=x_scale), y=alt.Y(y, title=_clean_label(y), scale=y_scale))
                )
            else:
                trend = (
                    smooth_base.transform_regression(x, y, method=smooth, groupby=groupby)
                    .mark_line(strokeWidth=3, opacity=0.9, clip=_clip)
                    .encode(x=alt.X(x, title=_clean_label(x), scale=x_scale), y=alt.Y(y, title=_clean_label(y), scale=y_scale))
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

    return (qplot,)


@app.cell(column=3, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Tests

    marimo also has support for Pytest. So let's make use of that! This helps any agent who is working on the project, but it also lets use test in CI via:

    ```
    pytest notebook.py
    ```
    """)
    return


@app.cell
def _(pd):
    # Default test dataset with common column types
    df_test = pd.DataFrame(
        {
            "x": [1, 2, 3, 4, 5],
            "y": [4, 5, 6, 7, 8],
            "c": ["a", "b", "a", "b", "a"],
            "s": [10, 20, 30, 40, 50],
            "o": [0.2, 0.4, 0.6, 0.8, 1.0],
        }
    )
    return (df_test,)


@app.cell
def _(df_test, qplot):
    ## Put pytests here.


    def test_scatter_encodes_x_and_y():
        spec = qplot(df_test, "x", "y").to_dict()
        assert spec["mark"]["type"] == "point"
        assert spec["encoding"]["x"]["field"] == "x"
        assert spec["encoding"]["y"]["field"] == "y"


    def test_histogram_when_y_omitted():
        spec = qplot(df_test, "x").to_dict()
        assert spec["mark"]["type"] == "bar"
        assert "bin" in spec["encoding"]["x"]
        assert spec["encoding"]["y"]["aggregate"] == "count"


    def test_clean_labels_applied():
        spec = qplot(df_test, "x", "y").to_dict()
        assert spec["encoding"]["x"]["title"] == "x"
        assert spec["encoding"]["y"]["title"] == "y"


    def test_color_encoding():
        spec = qplot(df_test, "x", "y", color="c").to_dict()
        assert spec["encoding"]["color"]["field"] == "c"
        assert spec["encoding"]["color"]["title"] == "c"


    def test_size_encoding():
        spec = qplot(df_test, "x", "y", size="s").to_dict()
        assert spec["encoding"]["size"]["field"] == "s"


    def test_opacity_as_column():
        spec = qplot(df_test, "x", "y", opacity="o").to_dict()
        assert spec["encoding"]["opacity"]["field"] == "o"


    def test_opacity_as_float():
        spec = qplot(df_test, "x", "y", opacity=0.3).to_dict()
        assert spec["mark"]["opacity"] == 0.3


    def test_group_uses_detail():
        spec = qplot(df_test, "x", "y", mark="line", group="c").to_dict()
        assert spec["encoding"]["detail"]["field"] == "c"


    def test_bins_param():
        spec = qplot(df_test, "x", bins=10).to_dict()
        assert spec["encoding"]["x"]["bin"]["maxbins"] == 10


    def test_title_and_subtitle():
        spec = qplot(df_test, "x", "y", title="Hello", subtitle="World").to_dict()
        assert spec["title"]["text"] == "Hello"
        assert spec["title"]["subtitle"] == "World"


    def test_actions_disabled_by_default():
        spec = qplot(df_test, "x", "y").to_dict()
        assert spec["usermeta"]["embedOptions"]["actions"] == False


    def test_actions_enabled():
        spec = qplot(df_test, "x", "y", actions=True).to_dict()
        assert spec["usermeta"]["embedOptions"]["actions"] == True


    def test_width_and_height():
        spec = qplot(df_test, "x", "y", width=400, height=300).to_dict()
        assert spec["width"] == 400
        assert spec["height"] == 300


    def test_smooth_adds_layer():
        spec = qplot(df_test, "x", "y", smooth="loess").to_dict()
        assert "layer" in spec
        assert len(spec["layer"]) == 2


    def test_mark_scatter():
        assert qplot(df_test, "x", "y", mark="scatter").to_dict()["mark"]["type"] == "point"


    def test_mark_circle():
        assert qplot(df_test, "x", "y", mark="circle").to_dict()["mark"]["type"] == "circle"


    def test_mark_line():
        assert qplot(df_test, "x", "y", mark="line").to_dict()["mark"]["type"] == "line"


    def test_mark_bar():
        assert qplot(df_test, "x", "y", mark="bar").to_dict()["mark"]["type"] == "bar"


    def test_invalid_mark_raises():
        try:
            qplot(df_test, "x", "y", mark="nope")
            assert False, "Should have raised"
        except ValueError as e:
            assert "Unknown mark" in str(e)


    def test_invalid_theme_raises():
        try:
            qplot(df_test, "x", "y", theme="nope")
            assert False, "Should have raised"
        except ValueError as e:
            assert "Unknown theme" in str(e)


    def test_mark_area():
        spec = qplot(df_test, "x", "y", mark="area").to_dict()
        assert spec["mark"]["type"] == "area"


    def test_mark_area_respects_opacity():
        spec = qplot(df_test, "x", "y", mark="area", opacity=0.5).to_dict()
        assert spec["mark"]["opacity"] == 0.5


    def test_mark_step():
        spec = qplot(df_test, "x", "y", mark="step").to_dict()
        assert spec["mark"]["type"] == "line"
        assert spec["mark"]["interpolate"] == "step"
        assert spec["mark"]["strokeWidth"] == 2


    def test_tooltip_encoding():
        spec = qplot(df_test, "x", "y", tooltip=["x", "y", "c"]).to_dict()
        tooltip_fields = [t["field"] for t in spec["encoding"]["tooltip"]]
        assert tooltip_fields == ["x", "y", "c"]


    def test_tooltip_none_by_default():
        spec = qplot(df_test, "x", "y").to_dict()
        assert "tooltip" not in spec["encoding"]


    def test_pipe_works():
        spec = df_test.pipe(qplot, "x", "y", color="x").to_dict()
        assert spec["encoding"]["color"]["field"] == "x"


    def test_x_lim():
        spec = qplot(df_test, "x", "y", x_lim=(0, 100)).to_dict()
        assert spec["encoding"]["x"]["scale"]["domain"] == [0, 100]


    def test_y_lim():
        spec = qplot(df_test, "x", "y", y_lim=(0, 50)).to_dict()
        assert spec["encoding"]["y"]["scale"]["domain"] == [0, 50]


    def test_partial_x_lim():
        spec = qplot(df_test, "x", "y", x_lim=(None, 100)).to_dict()
        assert spec["encoding"]["x"]["scale"]["domain"] == [None, 100]


    def test_partial_y_lim():
        spec = qplot(df_test, "x", "y", y_lim=(5, None)).to_dict()
        assert spec["encoding"]["y"]["scale"]["domain"] == [5, None]


    def test_lim_default_none():
        spec = qplot(df_test, "x", "y").to_dict()
        assert "scale" not in spec["encoding"]["x"]
        assert "scale" not in spec["encoding"]["y"]


    def test_lim_with_smooth():
        spec = qplot(df_test, "x", "y", x_lim=(0, 10), smooth="loess").to_dict()
        assert "layer" in spec
        for layer in spec["layer"]:
            assert layer["encoding"]["x"]["scale"]["domain"] == [0, 10]

    return


@app.cell(column=4)
def _():
    return


if __name__ == "__main__":
    app.run()
