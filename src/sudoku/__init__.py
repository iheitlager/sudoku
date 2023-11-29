# Some helper lists to iterate through houses
# space over compute
#################################################

# return columns' group of vertical cells
all_columns = [[(i, j) for i in range(9)] for j in range(9)]

# same for rows groups of horizontal cells
all_rows = [[(i, j) for j in range(9)] for i in range(9)]

# same for blocks, also called boxes
# this list comprehension is unreadable, but quite cool!
all_blocks = [[((i//3) * 3 + j//3, (i % 3)*3+j % 3)
               for j in range(9)] for i in range(9)]

# combine three to houses, also called containers
all_houses = all_columns+all_rows+all_blocks

# just get all coordinates for the grid
all_grid =  [(i, j) for i in range(9) for j in range(9)]

# get all candidate values
all_values = [i+1 for i in range(9)]


def cell(i, j, o_i=0, o_j=0):
    '''
    calculates one dimensional index with offset
    '''
    return (i+o_i)*9+j+o_j


def column_score(n, grid):
    try:
        return len(set(grid[i][j] for (i, j) in all_columns[n] if grid[i][j] > 0))
    except TypeError:
        return len(set(grid[i][j][0] for (i, j) in all_columns[n] if len(grid[i][j]) == 1))


def row_score(n, grid):
    try:
        return len(set(grid[i][j] for (i, j) in all_rows[n] if grid[i][j] > 0))
    except TypeError:
        return len(set(grid[i][j][0] for (i, j) in all_rows[n] if len(grid[i][j]) == 1))


def block_score(n, grid):
    try:
        return len(set(grid[i][j] for (i, j) in all_blocks[n] if grid[i][j] > 0))
    except TypeError:
        return len(set(grid[i][j][0] for (i, j) in all_blocks[n] if len(grid[i][j]) == 1))


def grid_score(grid):
    return sum(column_score(n, grid)+row_score(n, grid)+block_score(n, grid) for n in range(9))


def is_solved(grid):
    return grid_score(grid) == 3*9*9


def list_houses(i, j):
    '''
    Get the horizontal, vertical and block groups from a cell
    '''
    return [all_rows[i], all_columns[j], all_blocks[i // 3 * 3 + j // 3]]


def values_from_houses(i, j, grid):
    try:
        return set(grid[k][m] for house in list_houses(i, j) for (k, m) in house if grid[k][m] != 0)
    except TypeError:
        return set(grid[k][m][0] for house in list_houses(i, j) for (k, m) in house if len(grid[k][m]) == 1)


def houses_from_cell(i, j):
    return all_rows[i]+all_columns[j]+all_blocks[i // 3 * 3 + j // 3]

def n_from_houses(i, j, grid):
    return n_from_cells(houses_from_cell(i, j), grid)


def n_from_cells(cells, grid):
    '''
    Retrieve all unique candidates from cells
    '''
    numbers = []
    for (i, j) in cells:
        numbers += grid[i][j]
    return list(set(numbers))


def remove_n_from_cells(n, cells, grid):
    count = 0
    for (i, j) in cells:
        if n in grid[i][j]:
            grid[i][j].remove(n)
            count += 1
    return count


def column_score_list(n, ll):
    return len(set(ll[cell(i, j)] for (i, j) in all_columns[n] if ll[cell(i, j)] > 0))


def row_score_list(n, ll):
    return len(set(ll[cell(i, j)] for (i, j) in all_rows[n] if ll[cell(i, j)] > 0))


def block_score_list(n, ll):
    return len(set(ll[cell(i, j)] for (i, j) in all_blocks[n] if ll[cell(i, j)] > 0))


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
    try:
        return sum(len(grid[i][j])-1 for (i, j) in all_grid)
    except TypeError:
        return sum(9 for (i, j) in all_grid if grid[i][j] == 0)


def n_range(grid):
    try:
        return list(set(grid[i][j][0] for (i, j) in all_grid if len(grid[i][j]) == 1))
    except TypeError:
        return list(set(grid[i][j] for (i, j) in all_grid if grid[i][j] != 0))

def n_complete(grid):
    ret = []
    try:
        t = [grid[i][j][0] for (i, j) in all_grid if len(grid[i][j]) == 1]
    except TypeError:
        t = [grid[i][j] for (i, j) in all_grid if grid[i][j] != 0]
    for k in range(1,10):
        ret.append((k, sum(x == k for x in t)))
    return list(x for x, y in ret if y ==9)

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