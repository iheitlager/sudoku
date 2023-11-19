def read_matrix(filename):
    """Read a matrix from a filename.
    
    Note: wraps generic get_matrix method.
    """

    with open(filename, "r") as f:
        content = f.readlines()
    return get_matrix(content)


def get_matrix(content):
    """Return a list of lists containing the content of text.

    Note: each line of the text corresponds to a list. Each item in
    the list is from splitting the line of text by the delimiter ' ' or ','.
    Empty values are either 0 or . This is a fairly robust parser.
    """

    if type(content) == str: # split textblob into list of lines
        content = content.splitlines()

    lines = []
    for line in content:
        new_line = line.strip()    # Strip any leading or trailing whitespace
        new_line = new_line.replace(".", "0") # dots are zero's
        new_line = new_line.replace(",", "") # comma's are seperators
        new_line = new_line.replace(" ", "") # spaces are seperators
        if new_line:
            new_line = [int(x) for x in new_line]
            lines.append(new_line)

    return lines
