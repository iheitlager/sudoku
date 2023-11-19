# Simple test script to test our simple_sudoku solver

import copy
import simple_sudoku as ss


def test_grid_exists():
    assert len(ss.sudoku_grid) == 9


def test_is_valid():
    assert ss.is_valid(ss.sudoku_grid, 0, 0, 3)

def test_find_empty_cell():
    assert ss.find_empty_cell(ss.sudoku_grid)  == (0,0)

def test_is_complete():
    assert ss.is_complete(ss.sudoku_grid)  == False

def test_count_nonzero():
    assert ss.count_nonzero(ss.sudoku_grid)  == 27

def test_solve():
    g = copy.deepcopy(ss.sudoku_grid)
    assert ss.solve_sudoku(g) == True
    assert ss.is_complete(g) == True
    assert ss.count_nonzero(g) == 81
    assert ss.find_empty_cell(g) == (None, None)    