import sudoku as ss
from sudoku.solvers import backtracking as solver

problem_grid = [
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

solution_grid = [
    [4, 6, 8, 7, 3, 5, 1, 9, 2],
    [3, 5, 2, 6, 1, 9, 7, 8, 4],
    [7, 9, 1, 8, 4, 2, 3, 5, 6],
    [8, 3, 9, 2, 7, 4, 6, 1, 5],
    [1, 2, 6, 5, 8, 3, 9, 4, 7],
    [5, 4, 7, 9, 6, 1, 8, 2, 3],
    [6, 8, 4, 1, 2, 7, 5, 3, 9],
    [9, 1, 3, 4, 5, 6, 2, 7, 8],
    [2, 7, 5, 3, 9, 8, 4, 6, 1]
]

def test_solve():
    g = problem_grid.copy()
    assert solver.solve(g)
    assert ss.is_solved(g)
    assert ss.n_nonzero(g) == 81
    assert ss.find_empty_cell(g) == (None, None)
    assert solver.iterations == 2522
    assert ss.is_complete(g)
    # solved is solved
    assert solver.solve(g)
    assert solver.iterations == 2522
    assert g == solution_grid
    
