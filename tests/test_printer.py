from contextlib import redirect_stdout
import io

from sudoku.printer import display_grid

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

def test_display_grid():
    f = io.StringIO()
    with redirect_stdout(f):
        display_grid(sudoku_grid)
        out = f.getvalue()
        assert out == sudoku_string
