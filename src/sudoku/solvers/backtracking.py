from sudoku import find_empty_cell, is_complete, values_from_houses

iterations = 0

def solve(grid):
    global iterations
    
    if is_complete(grid):
        return True
    
    iterations += 1

    row, col = find_empty_cell(grid)
    for num in range(1, 10):
         if num not in values_from_houses(row, col, grid):
            grid[row][col] = num

            if solve(grid):
                return True

            grid[row][col] = 0

    return False
