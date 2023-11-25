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
            assert(cell(i, j, row, col) == (row+i)*9+col+j for i in range(3) for j in range(3))
