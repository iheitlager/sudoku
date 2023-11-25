# Taken from https://www.adrian.idv.hk/2019-01-30-simanneal/
# undid it from numpy reliance

import random
from simanneal import Annealer
from sudoku import to_list, all_blocks, cell;
from sudoku.solvers import heuristic



# FIXME: make sure we accept the grid instead of list
def initial_solution(problem):
    """provide sudoku problem, generate an init solution by randomly filling
    each sq block without considering row/col consistency"""
    solution = problem.copy()
    for block in range(9):
#        indices = block_indices(block)
        indices = [i*9+j for (i, j) in all_blocks[block]]
#        block = problem[indices]
        block = [problem[i] for i in indices]
        zeros = [i for i in indices if problem[i] == 0]
        to_fill = [i for i in range(1, 10) if i not in block]
        random.shuffle(to_fill)
        for index, value in zip(zeros, to_fill):
            solution[index] = value
    return solution



class Sudoku_Sq(Annealer):
    def __init__(self, grid):
        problem = to_list(grid)
        self.problem = problem
        state = initial_solution(problem)
        super().__init__(state)
    def move(self):
        """randomly swap two cells in a random square"""
        block = random.randrange(9)
        indices = [(i*9+j) for (i, j) in all_blocks[block] if self.problem[i*9+j] == 0]
        m, n = random.sample(indices, 2)
        self.state[m], self.state[n] = self.state[n], self.state[m]
    def energy(self):
        """calculate the number of violations: assume all rows are OK"""
        column_score = lambda n: -len(set(self.state[cell(i, n)] for i in range(9)))
        row_score = lambda n: -len(set(self.state[cell(n, i)] for i in range(9)))
        score = sum(column_score(n)+row_score(n) for n in range(9))
        if score == -2*9*9:
            self.user_exit = True # early quit, we found a solution
        return score
    


def solve(sudoku_grid):
    sudoku = Sudoku_Sq(sudoku_grid)
    sudoku.copy_strategy = "method"

    sudoku.Tmax = 0.5
    sudoku.Tmin = 0.05
    sudoku.steps = 100000
    sudoku.updates = 100
    state, e = sudoku.anneal()
    print("\n")

    print("E=%f (expect -162)" % e)
    for i in range(9):
        for j in range(9):
            sudoku_grid[i][j] = state[i*9+j]
    return True