from qplot import qplot
import altair as alt


def test_qplot_importable():
    assert callable(qplot)


def test_scatter():
    import pandas as pd
    df = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})
    chart = qplot(df, "x", "y")
    assert isinstance(chart, alt.Chart)


def test_histogram():
    import pandas as pd
    df = pd.DataFrame({"x": [1, 2, 3, 4, 5]})
    chart = qplot(df, "x")
    assert isinstance(chart, alt.Chart)
