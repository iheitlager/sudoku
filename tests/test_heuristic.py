from sudoku.solvers import heuristic

def test_allgrid():
    assert len(heuristic.all_grid) == 81


def test_all_columns():
    assert len(heuristic.all_columns) == 9


def test_all_rows():
    assert len(heuristic.all_rows) == 9


def test_all_blocks():
    assert len(heuristic.all_blocks) == 9


def test_all_houses():
    assert len(heuristic.all_houses) == 9+9+9