#! /usr/bin/env python3

"""
Solve day 8
"""

from collections import defaultdict
from utils import input_lines

# A  B   (children ...) METADATA
# A = number children
# B = number of metadata

def sum_metadata(data):
    numchildren = data[0]
    nummeta = data[1]
    data = data[2:]
    if numchildren == 0:
        meta = data[:nummeta]
        data = data[nummeta:]
        return data, sum(meta)
    total = 0
    for child in range(numchildren):
        data, _total = sum_metadata(data)
        total += _total
    meta = data[:nummeta]
    data = data[nummeta:]
    total += sum(meta)
    return data, total


def sum_weightedvalue(data):
    numchildren = data[0]
    nummeta = data[1]
    data = data[2:]
    childvalues = []
    if numchildren == 0:
        meta = data[:nummeta]
        data = data[nummeta:]
        return data, sum(meta)
    for child in range(numchildren):
        data, _total = sum_weightedvalue(data)
        childvalues.append(_total)
    meta = data[:nummeta]
    data = data[nummeta:]
    total = 0
    for m in meta:
        index = m - 1
        if index < numchildren:
            total += childvalues[index]
    return data, total



def do_part_1(day, test=False):
    lines = input_lines(day, test=test)
    data = list(map(int, lines[0].split()))
    print(sum_metadata(data))
    return


def do_part_2(day, test=False):
    lines = input_lines(day, test=test)
    data = list(map(int, lines[0].split()))
    print(sum_weightedvalue(data))
    return


if __name__ == "__main__":
    do_part_1(8, test=False)
    do_part_2(8, test=False)
