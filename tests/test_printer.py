from contextlib import redirect_stdout
import io

from sudoku import printer

sudoku_grid = [
    [0, 6, 0, 0, 0, 0, 1, 9, 0],
    [0, 0, 2, 6, 1, 0, 0, 0, 4],
    [7, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 7, 0, 0, 1, 0],
    [0, 0, 6, 0, 8, 3, 0, 0, 0],
    [5, 4, 0, 0, 6, 0, 0, 0, 3],
    [0, 8, 0, 0, 2, 7, 0, 3, 9],
    [0, 0, 0, 4, 0, 0, 0, 7, 8],
    [0, 0, 0, 0, 0, 0, 4, 0, 0]
]

sudoku_string = '''0 6 0 | 0 0 0 | 1 9 0 
0 0 2 | 6 1 0 | 0 0 4 
7 0 1 | 0 0 0 | 0 0 0 
------+-------+------
0 0 0 | 0 7 0 | 0 1 0 
0 0 6 | 0 8 3 | 0 0 0 
5 4 0 | 0 6 0 | 0 0 3 
------+-------+------
0 8 0 | 0 2 7 | 0 3 9 
0 0 0 | 4 0 0 | 0 7 8 
0 0 0 | 0 0 0 | 4 0 0 
'''

single_string = "060000190002610004701000000000070010006083000540060003080027039000400078000000400"

python_string = '''sudoku_grid = [
    [0, 6, 0, 0, 0, 0, 1, 9, 0],
    [0, 0, 2, 6, 1, 0, 0, 0, 4],
    [7, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 7, 0, 0, 1, 0],
    [0, 0, 6, 0, 8, 3, 0, 0, 0],
    [5, 4, 0, 0, 6, 0, 0, 0, 3],
    [0, 8, 0, 0, 2, 7, 0, 3, 9],
    [0, 0, 0, 4, 0, 0, 0, 7, 8],
    [0, 0, 0, 0, 0, 0, 4, 0, 0]
]
'''

def test_display_grid():
    f = io.StringIO()
    with redirect_stdout(f):
        printer.display_grid(sudoku_grid)
        out = f.getvalue()
        assert out == sudoku_string


def test_display_pygrid():
    f = io.StringIO()
    with redirect_stdout(f):
        printer.display_pylist(sudoku_grid)
        out = f.getvalue()
        assert out == python_string


def test_as_single_string():
    result = printer.as_string(sudoku_grid)
    assert result == single_string


def test_display_list():
    f = io.StringIO()
    with redirect_stdout(f):
        printer.display_list(single_string)
        out = f.getvalue()
        assert out == sudoku_string
