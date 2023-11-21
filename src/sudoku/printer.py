# This file contains the printer functions

def display_grid(grid):
    '''Display the grid'''
    for i in range(9):
        if i in [3, 6]:
            print ('------+-------+------')
        print_line = ""
        for j in range(9):
            print_line += str(grid[i][j])
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
