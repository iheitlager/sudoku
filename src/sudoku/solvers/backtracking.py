from sudoku import find_empty_cell, is_complete, values_from_houses

iterations = 0

def solve(grid):
    global iterations
    
    if is_complete(grid):
        return True
    
    iterations += 1
    if iterations % 500 == 0:
        print('Iterations: ' + str(iterations))

    i, j = find_empty_cell(grid)
    for num in range(1, 10):
         if num not in values_from_houses(i, j, grid):
            grid[i][j] = num

            if solve(grid):
                return True

            grid[i][j] = 0

    return False
