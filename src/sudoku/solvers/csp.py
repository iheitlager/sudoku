from sudoku import is_solved
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
        problem.addConstraint(AllDifferentConstraint(),[row*9+i for i in range(9)])
    for col in range(9):
        problem.addConstraint(AllDifferentConstraint(),[col+i*9 for i in range(9)])
    for row in range(0,9,3):
        for col in range(0,9,3):
            problem.addConstraint(AllDifferentConstraint(),[(row+i)*9+col+j for i in range(3) for j in range(3)])

    result = problem.getSolution()
    for i in range(9):
        for j in range(9):
            sudoku_grid[i][j] = result[i*9+j]
    return True
