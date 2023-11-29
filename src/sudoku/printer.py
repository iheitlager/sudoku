# This file contains the printer functions
import sudoku

def display_grid(grid):
    '''
    Display the grid
    '''
    for i in range(9):
        if i in [3, 6]:
            print ('------+-------+------')
        print_line = ""
        for j in range(9):
            if isinstance(grid[i][j], list) and len(grid[i][j]) == 1:
                print_line += str(grid[i][j][0])
            else:
                print_line += str(grid[i][j])
            print_line += " | " if j in [2, 5] else " "
        print(print_line)


def display_supergrid(grid, simple=False):
    for i in range(9):
        if i in [3, 6]:
            print ('------------+-------------+------------')
        else:
            print ('            |             |            ')
        for row in range(0,3):
            line = ""
            for j in range(9):
                for col in range(0,3): 
                    num = row*3+col+1
                    if isinstance(grid[i][j], int):
                        line += str(num) if num == grid[i][j] else '.'
                    else:
                        zero = ' ' if len(grid[i][j]) == 1 and simple else '.'
                        line += str(num) if num in grid[i][j] else zero
                line += ' '
                if j in (2,5):
                    line += '| '
            print(line)
    print("            |             |            ")



def display_list(ll):
    '''
    Display a list as grid
    '''
    for i in range(9):
        if i in [3, 6]:
            print ('------+-------+------')
        print_line = ""
        for j in range(9):
            print_line += str(ll[i*9+j])
            print_line += " | " if j in [2, 5] else " "
        print(print_line)


def display_pylist(grid):
    '''
    Display the grid as a python readable list
    '''
    print("sudoku_grid = [")
    for row in grid[:-1]:
        print("    [%s]," % ', '.join([str(x) for x in row]))
    print("    [%s]" % ', '.join([str(x) for x in grid[-1]]))
    print("]")


def display_file(grid, comment=None, sep='', zero='.'):
    '''
    Display the grid as a file readable
    '''
    if comment:
        print("#"+comment)
    for row in grid:
        try:
            print(sep.join(str(x[0]) if len(x)==1 else zero for x in row))
        except TypeError:
            print(sep.join(str(x) if x!=0 else zero for x in row))


def as_string(grid):
    '''
    Return as single line string
    '''
    # return "".join([str(cell) for row in grid for cell in row])
    result = ""
    for row in grid:
        for cell in row:
            result += str(cell)
    return result


def display_stats(grid):
    nz = sudoku.n_nonzero(grid)
    print("Filled in: %d, open: %d (sum=%d)" % (nz, 81-nz, 81))
    print("Grid score: %d (max=%d)" % (sudoku.grid_score(grid), 3*9*9))
    print("Values to eliminate: %d (max=%d)" % (sudoku.n_to_remove(grid), 9*9*9))
    print("Range: " + str(sudoku.n_range(grid)))
    print("Completed: " + str(sudoku.n_complete(grid)))