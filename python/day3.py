#! /usr/bin/env python3

"""
Solve day 3
"""

from collections import defaultdict
from utils import input_lines


"""
We represent the fabric as a dictionary. The keys are the coordinate-tuples
like (1,2), and the values are the number of times that piece of fabric
appears in a rectangle.
"""
fabric = defaultdict(int)


def register_rect(_id, x, y, width, height, record=fabric):
    """
    For each square in rectangle, add 1 to record dictionary.
    """
    for i in range(x, x+width):
        for j in range(y, y+height):
            record[(i,j)] += 1
    return


def check_overlaps(_id, x, y, width, height, record=fabric):
    """
    If _id has no overlaps in the fabric, print the _id and return True.
    """
    not_seen = True
    for i in range(x, x+width):
        for j in range(y, y+height):
            if record[(i,j)] != 1:
                not_seen = False
    if not_seen:
        print(_id)
    return not_seen


def parse_line(line):
    """
    A line is of the form

      #id @ x,y: widthxheight
    """
    _id, _, tail = line.partition("@")
    coords, _, dims = tail.partition(":")
    x, y = list(map(int, coords.split(",")))
    width, height = list(map(int, dims.split("x")))
    return (_id, x, y, width, height)


def do_part_1(test=False, record=fabric):
    """
    Solves part 1
    """
    lines = input_lines(3, test=test)
    for line in lines:
        register_rect(*parse_line(line), record=record)
    total = 0
    for val in record.values():
        if val > 1:
            total += 1
    print(total)
    return total


def test_part_1():
    """
    Tests part 1
    """
    testfabric = defaultdict(int)
    assert do_part_1(test=True, record=testfabric) == 4
    return


def do_part_2(record=fabric):
    """
    Solves part 2
    """
    lines = input_lines(3)
    for line in lines:
        if check_overlaps(*parse_line(line), record=record):
            return
    return


def print_record(record=fabric):
    """
    To visualize (part) of the blanket.
    For my data, the top left 50x50 part happens to be boring.
    """
    out = ""
    for i in range(50):
        for j in range(50):
            out += str(record[(i,j)])
        out += "\n"
    print(out)
    return


def make_picture(record=fabric):
    """
    To visualize the blanket.
    Elves have terrible ideas for efficiency.
    """
    import matplotlib.pyplot as plt
    mat = []
    for i in range(1000):
        row = []
        for j in range(1000):
            row += [record[(i,j)]]
        mat += [row]
    fig = plt.figure(figsize=(10,10))
    plt.matshow(mat, fignum=1)
    plt.axis('off')
    plt.savefig("day3.pdf", bbox_inches='tight')
    plt.show()



if __name__ == "__main__":
    #test_part_1()
    do_part_1()
    do_part_2()
    #print_record()
    #make_picture()
