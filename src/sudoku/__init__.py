# Some helper lists to iterate through houses
# space over compute
#################################################

# return columns' lists of cells
all_columns = [[(i, j) for j in range(9)] for i in range(9)]

# same for rows
all_rows = [[(i, j) for i in range(9)] for j in range(9)]

# same for blocks
# this list comprehension is unreadable, but quite cool!
all_blocks = [[((i//3) * 3 + j//3, (i % 3)*3+j % 3)
               for j in range(9)] for i in range(9)]

# combine three
all_houses = all_columns+all_rows+all_blocks

# just get all coordinates
all_grid =  [(i, j) for i in range(9) for j in range(9)]


def cell(i, j, o_i=0, o_j=0):
    '''
    calculates one dimensional index with offset
    '''
    return (i+o_i)*9+j+o_j


def n_nonzero(grid):
    return sum(grid[i][j] != 0 for (i, j) in all_grid)


def is_solved(grid):
    for (i, j) in all_grid:
        if isinstance(grid[i][j], list) and len(grid[i][j]) != 1:
             return False
        elif grid[i][j] == 0 :
            return False
    return True


def find_empty_cell(grid):
    # return next(((i, j) for (i, j) in all_grid if grid[i][j] == 0), (None, None))
    for (i, j) in all_grid:
        if grid[i][j] == 0:
            return i, j
    return None, None


def flatten(grid):
    for (i, j) in all_grid:
        if isinstance(grid[i][j], list) and len(grid[i][j]) == 1:
            grid[i][j] = grid[i][j][0]


def copy_fromlist(grid, ll):
    for i in range(9):
        for j in range(9):
            grid[i][j] = ll[i*9+j]


def to_list(grid):
    return [x for row in grid for x in row]