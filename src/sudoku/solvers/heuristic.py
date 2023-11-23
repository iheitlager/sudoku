# This is taken from https://github.com/gamescomputersplay/sudoku-solver
from sudoku import all_grid
import copy

# Some helper lists to iterate through houses
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


# Adding candidates as list instead of zeros
def pencil_in_numbers(puzzle):
    result = copy.deepcopy(puzzle)
    for (i, j) in all_grid:
        if puzzle[i][j] != 0:
            result[i][j] = [puzzle[i][j], ]
        else:
            result[i][j] = [i for i in range(1, 10)]
    return result


def simple_elimination(sudoku):
    count = 0
    for group in all_houses:
        for (i, j) in group:
            if len(sudoku[i][j]) == 1:
                for (i2, j2) in group:
                    if sudoku[i][j][0] in sudoku[i2][j2] and (i, j) != (i2, j2):
                        sudoku[i2][j2].remove(sudoku[i][j][0])
                        count += 1
    return count


def hidden_single(sudoku):

    def find_only_number_in_group(group, number):
        count = 0
        removed = 0
        i2, j2 = (-1, -1)
        for (i, j) in group:
            for n in sudoku[i][j]:
                if n == number:
                    count += 1
                    i2, j2 = (i, j)
        if count == 1 and (i2, j2) != (-1, -1) \
           and len(sudoku[i2][j2]) > 1:
            removed = len(sudoku[i2][j2]) - 1
            sudoku[i2][j2] = [number]
        return removed

    count = 0
    for number in range(1, 10):
        for group in all_houses:
            count += find_only_number_in_group(group, number)
    return count