# Some helper lists to iterate through houses
# space over compute
#################################################

# return columns' lists of cells
all_columns = [[(i, j) for i in range(9)] for j in range(9)]

# same for rows
all_rows = [[(i, j) for j in range(9)] for i in range(9)]

# same for blocks, also called boxesß
# this list comprehension is unreadable, but quite cool!
all_blocks = [[((i//3) * 3 + j//3, (i % 3)*3+j % 3)
               for j in range(9)] for i in range(9)]

# combine three to houses, also called containers
all_houses = all_columns+all_rows+all_blocks

# just get all coordinates
all_grid =  [(i, j) for i in range(9) for j in range(9)]

all_values = [i+1 for i in range(9)]


def cell(i, j, o_i=0, o_j=0):
    '''
    calculates one dimensional index with offset
    '''
    return (i+o_i)*9+j+o_j


def column_score(n, grid):
    try:
        return len(set(grid[i][j] for (i, j) in all_columns[n]))
    except TypeError:
        return len(set(grid[i][j][0] for (i, j) in all_columns[n] if len(grid[i][j]) == 1))


def row_score(n, grid):
    try:
        return len(set(grid[i][j] for (i, j) in all_rows[n]))
    except TypeError:
        return len(set(grid[i][j][0] for (i, j) in all_rows[n] if len(grid[i][j]) == 1))


def block_score(n, grid):
    try:
        return len(set(grid[i][j] for (i, j) in all_blocks[n]))
    except TypeError:
        return len(set(grid[i][j][0] for (i, j) in all_blocks[n] if len(grid[i][j]) == 1))


def grid_score(grid):
    return sum(column_score(n, grid)+row_score(n, grid)+block_score(n, grid) for n in range(9))


def is_solved(grid):
    return grid_score(grid) == 3*9*9


def list_houses(i, j):
    return [all_rows[i], all_columns[j], all_blocks[i // 3 * 3 + j // 3]]


def values_from_houses(i, j, grid):
    try:
        return set(grid[k][m] for house in list_houses(i, j) for (k, m) in house if grid[k][m] != 0)
    except TypeError:
        return set(grid[k][m][0] for house in list_houses(i, j) for (k, m) in house if len(grid[k][m]) == 1)



def column_score_list(n, ll):
    return len(set(ll[cell(i, j)] for (i, j) in all_columns[n]))


def row_score_list(n, ll):
    return len(set(ll[cell(i, j)] for (i, j) in all_rows[n]))


def block_score_list(n, ll):
    return len(set(ll[cell(i, j)] for (i, j) in all_blocks[n]))


def list_score(ll):
    return sum(column_score_list(n, ll)+row_score_list(n, ll)+block_score_list(n, ll) for n in range(9))


def n_nonzero(grid):
    try:
        return sum(grid[i][j][0] != 0 for (i, j) in all_grid if len(grid[i][j]) == 1)
    except (IndexError, TypeError):
    # if isinstance(grid[0][0], list):
    #     return sum(grid[i][j][0] != 0 for (i, j) in all_grid if len(grid[i][j]) == 1)
    # else:
        return sum(grid[i][j] != 0 for (i, j) in all_grid)


def list_nonzero(grid):
    try:
        return [(i, j) for (i, j) in all_grid if grid[i][j][0] != 0 and len(grid[i][j] == 1)]
    except TypeError:
        return [(i, j) for (i, j) in all_grid if grid[i][j] != 0]


def n_to_remove(grid):
    return sum(len(grid[i][j])-1 for (i, j) in all_grid)


def is_complete(grid):
    for (i, j) in all_grid:
        if isinstance(grid[i][j], list) and len(grid[i][j]) != 1:
             return False
        elif grid[i][j] == 0:
            return False
    return True


def find_empty_cell(grid):
    # return next(((i, j) for (i, j) in all_grid if grid[i][j] == 0), (None, None))
    for (i, j) in all_grid:
        if isinstance(grid[i][j], list) and len(grid[i][j]) > 1:
            return i, j
        if grid[i][j] == 0:
            return i, j
    return None, None


def flatten(grid, to_grid=None):
    if not to_grid:
        to_grid=grid
    for (i, j) in all_grid:
        if isinstance(grid[i][j], list):
            if len(grid[i][j]) == 1:
                to_grid[i][j] = grid[i][j][0]
            else:
                to_grid[i][j] = 0


def unflatten(grid, to_grid=None):
    if not to_grid:
        to_grid=grid
    for (i, j) in all_grid:
        if isinstance(grid[i][j], int):
            if grid[i][j] >= 1:
                to_grid[i][j] = [grid[i][j]]
            else:
                to_grid[i][j] = all_values


def copy_fromlist(grid, ll):
    for i in range(9):
        for j in range(9):
            grid[i][j] = ll[cell(i, j)]


def list_grid(grid):
    return [x for row in grid for x in row]