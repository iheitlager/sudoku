# 
# This file contains a simple standalone sudoku solver
# deliberately it is without libraries and all self contained
# this is a dept-first backtracking search algorithm
# it searches on first empty cell and tries first unique number in cell
#
# Example is take from:
# https://saturncloud.io/blog/python-sudoku-wave-function-collapse-algorithm-implementation/
# 
# simply use: python simple_sudoky.py to run this program
#

iterations = 0

def display_grid(grid):
    '''Display the grid'''
    for i in range(9):
        if i in [3, 6]:
            print ('------+-------+------')
        l = ""
        for j in range(9):
            l += str(grid[i][j])
            l += " | " if j in [2, 5] else " "
        print(l)

def solve_sudoku(grid):
    global iterations
    iterations += 1

    if is_complete(grid):
        return True

    row, col = find_empty_cell(grid)
    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True

            grid[row][col] = 0

    return False

def count_nonzero(grid):
    n = 0
    for row in range(9):
        for col in range(9):
            if grid[row][col] != 0:
                n += 1
    return n

def is_complete(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return False
    return True

def find_empty_cell(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None, None

def is_valid(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False

    return True

# Parool Dinsdag 19 sept ****
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

print("Fill before rate: {0:d}".format(count_nonzero(sudoku_grid)))
solve_sudoku(sudoku_grid)
fr = count_nonzero(sudoku_grid)
frp = fr / 81 * 100.0
print("Fill after rate: {0:d} ({1:0.0f}%)".format(fr, frp))
print("Iterations: {0:d}".format(iterations))
display_grid(sudoku_grid)