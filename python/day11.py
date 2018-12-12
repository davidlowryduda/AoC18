#! /usr/bin/env python3

"""
Solve day 11
"""

from utils import input_lines

def power_level(x, y, serial=8):
    """
    A nonsense sequence of steps described in the puzzle instructions.
    """
    rackID = x + 10
    level = rackID * y
    level += serial
    level *= rackID
    level = (level // 100) % 10
    level -= 5
    return level


def compute_power_levels(serial):
    """
    Create a grid where grid[(x,y)] has the power_level at position (x,y).
    """
    grid = dict()
    for x in range(1, 301):
        for y in range(1, 301):
            grid[(x, y)] = power_level(x, y, serial=serial)
    return grid


def compute_sized_powerlevel(grid, x, y, size=3):
    """
    Compute combined powerlevel for sizexsize grid with topleft element (x,y).
    """
    total_power_level = 0
    for i in range(size):
        for j in range(size):
            total_power_level += grid[(x+i, y+j)]
    return total_power_level


def find_largest_trio(grid):
    """
    Find the largest 3x3 grid value.
    """
    record = 0
    record_tuple = (0,0)
    for x in range(1, 298):
        for y in range(1, 298):
            candidate_power = compute_sized_powerlevel(grid, x, y)
            if candidate_power > record:
                record = candidate_power
                record_tuple = (x, y)
    return record, record_tuple


def find_largest_anysize(grid):
    """
    Find the largest sizexsize grid value.
    """
    record = 0
    record_tuple = (0, 0, 0)
    for x in range(1, 298):
        print("On x =", x)
        for y in range(1, 298):
            maxsize = min(300-x, 300-y)
            cand_record, cand_tuple = find_largest_anysize_at_xy(grid, x, y)
            if cand_record > record:
                record = cand_record
                record_tuple = cand_tuple
    return record, record_tuple


def find_largest_anysize_at_xy(grid, x, y):
    """
    Finds the largest sizexsize grid with top-left location (x,y).
    """
    maxsize = min(300 - x, 300 - y)
    record = grid[(x,y)]
    record_tuple = (x, y, 1)
    prevsize = record
    for size in range(2, maxsize + 1):
        cand = prevsize
        for i in range(size):
            cand += grid[(x+i, y+size-1)]
            cand += grid[(x+size-1, y+i)]
        cand -= grid[(x+size-1, y+size-1)]
        prevsize = cand
        if cand > record:
            record = cand
            record_tuple = (x, y, size)
    return record, record_tuple



def do_part_1(day, test=False):
    #TESTSERIAL = 18
    #TESTSERIAL = 42
    MYSERIAL = 5719
    grid = compute_power_levels(MYSERIAL)
    print(find_largest_trio(grid)[1])
    return


def do_part_2(day, test=False):
    #TESTSERIAL = 18
    MYSERIAL = 5719
    grid = compute_power_levels(MYSERIAL)
    print(find_largest_anysize(grid))
    return


if __name__ == "__main__":
    do_part_1(11, test=False)
    do_part_2(11, test=False)
