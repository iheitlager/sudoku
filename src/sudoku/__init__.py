# just get all coordinates
all_grid =  [(i, j) for i in range(9) for j in range(9)]

def n_nonzero(grid):
    n = 0
    for (i, j) in all_grid:
        if grid[i][j] != 0:
            n += 1
    return n


def is_solved(grid):
    for (i, j) in all_grid:
        if isinstance(grid[i][j], list) and len(grid[i][j]) != 1:
             return False
        elif grid[i][j] == 0 :
            return False
    return True


def find_empty_cell(grid):
    for (i, j) in all_grid:
        if grid[i][j] == 0:
            return i, j
    return None, None


def flatten(grid):
    for (i, j) in all_grid:
        if isinstance(grid[i][j], list) and len(grid[i][j]) == 1:
            grid[i][j] = grid[i][j][0]