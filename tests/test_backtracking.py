import sudoku as ss
from sudoku.solvers import backtracking
import copy

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


def test_solve():
    g = copy.deepcopy(sudoku_grid)
    assert backtracking.solve(g)
    assert ss.is_complete(g)
    assert ss.count_nonzero(g) == 81
    assert ss.find_empty_cell(g) == (None, None)
