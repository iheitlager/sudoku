# This is taken from https://github.com/gamescomputersplay/sudoku-solver
# rewrote it in simple 2D matrix code
# Check this https://sudoku.coach/en/learn/technique-overview

from sudoku import is_complete, flatten, \
    all_grid, all_houses, all_blocks, all_rows, all_columns, \
    all_values, \
    n_from_cells, remove_n_from_cells, \
    find_empty_cell, values_from_houses

# Adding candidates as list instead of zeros
def pencil_in_numbers(puzzle):
    result = puzzle.copy()
    for (i, j) in all_grid:
        if puzzle[i][j] != 0:
            result[i][j] = [puzzle[i][j], ]
        else:
            result[i][j] = [i for i in range(1, 10)]
    return result


# Heuristic number 1
# Eliminate singles from rows, columns and blocks
# Automatically leads to Last Digits and Naked Singles
def simple_elimination(grid):
    count = 0
    for group in all_houses:
        for (i, j) in group:
            if len(grid[i][j]) == 1:
                for (i2, j2) in group:
                    if grid[i][j][0] in grid[i2][j2] and (i, j) != (i2, j2):
                        grid[i2][j2].remove(grid[i][j][0])
                        count += 1
    return count


# Heuristic number 2
def hidden_single(grid):

    def find_only_number_in_group(group, number):
        count = 0
        removed = 0
        i2, j2 = (-1, -1)
        for (i, j) in group:
            for n in grid[i][j]:
                if n == number:
                    count += 1
                    i2, j2 = (i, j)
        if count == 1 and (i2, j2) != (-1, -1) \
           and len(grid[i2][j2]) > 1:
            removed = len(grid[i2][j2]) - 1
            grid[i2][j2] = [number]
        return removed

    count = 0
    for number in range(1, 10):
        for group in all_houses:
            count += find_only_number_in_group(group, number)
    return count

#Heuristic number 3 - point pairs/triples
def pointing_pairs(grid):
    count = 0
    for block in all_blocks:
        for line in all_columns + all_rows:
            sblock = set(block)
            sline = set(line)
            both = sblock.intersection(sline)
            if len(both) == 0:
                continue
            only_b = sblock.difference(both)
            only_l = sline.difference(both)

            n_both = n_from_cells(both, grid)
            n_only_b = n_from_cells(only_b, grid)
            n_only_l = n_from_cells(only_l, grid)

            for i in all_values:
                if i in n_both and i in n_only_b and i not in n_only_l:
                    count += remove_n_from_cells(i, list(only_b), grid)
                if i in n_both and i not in n_only_b and i in n_only_l:
                    count += remove_n_from_cells(i, list(only_l), grid)

    return count


# Heuristic number 4 - Brute force backtracking
def backtrack(grid):
    if is_complete(grid):
        return True

    i, j = find_empty_cell(grid)
    if (i, j) == (None, None):
        return True

    old_num = grid[i][j]
    for num in old_num:
        if num not in values_from_houses(i, j, grid):
            grid[i][j] = [num]

            if backtrack(grid):
                return True

            grid[i][j] = old_num

    return False

# 2. CSP
# brute force CSP solution for each cell:
# it covers hidden and naked pairs, triples, quads
################################################
def csp_list(house):

    perm = []

    # recurive func to get all permutations
    def append_permutations(sofar):
        nonlocal house
        for n in house[len(sofar)]:
            if len(sofar) == len(house) - 1:
                perm.append(sofar + [n])
            else:
                append_permutations(sofar + [n])

    append_permutations([])

    # filter out impossibble ones
    for i in range(len(perm))[::-1]:
        if len(perm[i]) != len(set(perm[i])):
            del perm[i]

    # which values are still there?
    out = []
    for i in range(len(house)):
        out.append([])
        for n in range(10):
            for p in perm:
                if p[i] == n and n not in out[i]:
                    out[i].append(n)
    return out


def csp(grid):
    count = 0
    for group in all_houses:
        house = []
        for (i, j) in group:
            house.append(grid[i][j])
        house_csp = csp_list(house)
        if house_csp != house:
            for n in range(len(group)):
                (i, j) = group[n]
                if grid[i][j] != house_csp[n]:
                    count += len(grid[i][j]) - len(house_csp[n])
                    grid[i][j] = house_csp[n]
    return count


cycles = 0
counts = [0, 0, 0, 0]

def solve(problem):
    '''
    Heuristic solver
    '''
    global cycles
    global counts

    grid = pencil_in_numbers(problem)
    
    while not is_complete(grid):
        cycles += 1
        c0 = simple_elimination(grid)
        counts[0] += c0
        c1 = hidden_single(grid)
        counts[1] += c1
        c2 = 0
        c2 = csp(grid)
        counts[2] += c2
        c3 = pointing_pairs(grid)
        counts[2] += c3

        if c0+c1+c2+c3 == 0:
            return False
        
    flatten(grid)
    return True