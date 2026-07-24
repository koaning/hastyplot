def test_import_qplot():
    from hastyplot import qplot

    assert callable(qplot)


def test_import_annotate():
    from hastyplot import annotate

    assert callable(annotate)
