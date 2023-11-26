# This file contains the printer functions

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


def display_file(grid, comment=None):
    '''
    Display the grid as a file readable
    '''
    if comment:
        print("#"+comment)
    for row in grid:
        try:
            print(''.join(str(x[0]) if len(x)==1 else '.' for x in row))
        except TypeError:
            print(''.join(str(x) if x!=0 else '.' for x in row))


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