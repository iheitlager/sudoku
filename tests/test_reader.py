from sudoku import reader


example1 = """.......92
...1...4.
9..24...7
8..7..15.
65.9.1.78
.74..8..6
3...95..1
.8...6...
79.......
"""

example1_alt = """. . . .. ..92
...1...4.
9..2400.7

8..7..15.

6,5,.,9,.,1,.,7,8
.74..,8,.,.,6


3...95..1
.8...6...
790000000
"""

example2 = """# this is a **** level puzzle from parool 2023-09-19
.6....19.
..261...4
7.1......
....7..1.
..6.83...
54..6...3
.8..27.39
...4...78
......4..
"""

example1_list = [
    [0,0,0,0,0,0,0,9,2],
    [0,0,0,1,0,0,0,4,0],
    [9,0,0,2,4,0,0,0,7],
    [8,0,0,7,0,0,1,5,0],
    [6,5,0,9,0,1,0,7,8],
    [0,7,4,0,0,8,0,0,6],
    [3,0,0,0,9,5,0,0,1],
    [0,8,0,0,0,6,0,0,0],
    [7,9,0,0,0,0,0,0,0]
]

example2_list = [
    [0,6,0,0,0,0,1,9,0],
    [0,0,2,6,1,0,0,0,4],
    [7,0,1,0,0,0,0,0,0],
    [0,0,0,0,7,0,0,1,0],
    [0,0,6,0,8,3,0,0,0],
    [5,4,0,0,6,0,0,0,3],
    [0,8,0,0,2,7,0,3,9],
    [0,0,0,4,0,0,0,7,8],
    [0,0,0,0,0,0,4,0,0]
]


def test_example1():
    m = reader.get_matrix(example1)
    assert len(m) == 9
    assert m[0] == [0,0,0,0,0,0,0,9,2]
    assert m == example1_list

    
def test_example1_alt():
    m = reader.get_matrix(example1_alt)
    assert m == example1_list


def test_example2():
    m = reader.get_matrix(example2)
    assert m == example2_list


def test_reader():
    # it is all relative from where pytest starts
    m = reader.read_matrix("./data/example1.txt")
    assert m == example1_list
    m = reader.read_matrix("./data/parool230919.txt")
    assert m == example2_list
