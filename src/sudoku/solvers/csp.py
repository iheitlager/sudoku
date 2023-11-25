from sudoku import is_solved, cell
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
        problem.addConstraint(AllDifferentConstraint(),[cell(row, j) for j in range(9)])
    for col in range(9):
        problem.addConstraint(AllDifferentConstraint(),[cell(i, col) for i in range(9)])
    for row in range(0,9,3):
        for col in range(0,9,3):
            problem.addConstraint(AllDifferentConstraint(),[cell(i, j, row, col) for i in range(3) for j in range(3)])

    result = problem.getSolution()
    for i in range(9):
        for j in range(9):
            sudoku_grid[i][j] = result[i*9+j]
    return True
