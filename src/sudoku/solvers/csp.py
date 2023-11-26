from sudoku import is_solved, cell, copy_fromlist
from sudoku import all_houses, all_grid, all_values
from constraint import Problem, BacktrackingSolver, AllDifferentConstraint


def solve(sudoku_grid):
    if is_solved(sudoku_grid):
        return True

    problem = Problem(BacktrackingSolver())
    for i in range(9):
        for j in range(9):
            if sudoku_grid[i][j] == 0:
                problem.addVariable(i*9+j, range(1,9+1))
            else:
                problem.addVariable(i*9+j, [sudoku_grid[i][j]])

    for row in range(9):
        problem.addConstraint(AllDifferentConstraint(),[row*9+j for j in range(9)])
    for col in range(9):
        problem.addConstraint(AllDifferentConstraint(),[i*9+col for i in range(9)])
    for row in range(0,9,3):
        for col in range(0,9,3):
            problem.addConstraint(AllDifferentConstraint(),[(i+row)*9+j+col for i in range(3) for j in range(3)])

    result = problem.getSolution()
    for i in range(9):
        for j in range(9):
            sudoku_grid[i][j] = result[i*9+j]
    return True



def solve2(sudoku_grid):
    if is_solved(sudoku_grid):
        return True

    problem = Problem(BacktrackingSolver())

    for (i, j) in all_grid:
        if sudoku_grid[i][j] == 0:
            problem.addVariable(cell(i, j), all_values)
        else:
            problem.addVariable(cell(i, j), [sudoku_grid[i][j]])

    for block in all_houses:
        problem.addConstraint(AllDifferentConstraint(), [cell(i, j) for (i, j) in block])

    result = problem.getSolution()
    copy_fromlist(sudoku_grid, result)
    return True
