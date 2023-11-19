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
