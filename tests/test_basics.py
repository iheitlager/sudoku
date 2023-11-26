import sudoku as ss

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

sudoku_list = [
    0, 6, 0, 0, 0, 0, 1, 9, 0,
    0, 0, 2, 6, 1, 0, 0, 0, 4,
    7, 0, 1, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 7, 0, 0, 1, 0,
    0, 0, 6, 0, 8, 3, 0, 0, 0,
    5, 4, 0, 0, 6, 0, 0, 0, 3,
    0, 8, 0, 0, 2, 7, 0, 3, 9,
    0, 0, 0, 4, 0, 0, 0, 7, 8,
    0, 0, 0, 0, 0, 0, 4, 0, 0
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

def test_allgrid():
    assert len(ss.all_grid) == 81


def test_find_empty_cell():
    assert ss.find_empty_cell(sudoku_grid) == (0, 0)


def test_is_solved():
    assert not ss.is_solved(sudoku_grid)


def test_n_nonzero():
    assert ss.n_nonzero(sudoku_grid) == 27


def test_to_list():
    assert ss.to_list(sudoku_grid) == sudoku_list


def test_cell():
    for i in range(9):
        for j in range(9):
            assert i*9+j == ss.cell(i, j)


def test_cell_offset():
    for row in range(0,9,3):
        for col in range(0,9,3):
            assert(ss.cell(i, j, row, col) == (row+i)*9+col+j for i in range(3) for j in range(3))


def test_all_columns():
    assert len(ss.all_columns) == 9


def test_all_rows():
    assert len(ss.all_rows) == 9


def test_all_blocks():
    assert len(ss.all_blocks) == 9


def test_all_houses():
    assert len(ss.all_houses) == 9+9+9


def test_grid_score():
    assert ss.grid_score(sudoku_grid) == 108
    assert ss.grid_score(solution_grid) == 243


def test_list_score():
    assert ss.list_score(sudoku_list) == 108
