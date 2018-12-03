#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Solve day 1.
"""

from utils import input_lines


def interpret_line(line):
    """
    Parses sign and num from line. Returns `(num, op)`, where op is the
    operation to perform on the line.
    """
    sign, num = line[0], line[1:]
    if sign == "+":
        op = _add
    elif sign == "-":
        op = _subtract
    else:
        raise ValueError("Sign is not +/-")
    return int(num), op


def _add(a, b):
    return a + b


def _subtract(a, b):
    return a - b


def do_part_1():
    """
    Solve the puzzle.
    """
    data = input_lines(1)
    total = 0
    for line in data:
        val, op = interpret_line(line)
        total = op(total, val)
    print(total)
    return total


def do_part_2():
    """
    Solve the puzzle... part 2.
    """
    data = input_lines(1)
    total = 0
    iters = 0              # Count iters
    seen = set()
    while iters < 10**7:   # so that it doesn't accidentally run forever
        for line in data:
            iters += 1
            val, op = interpret_line(line)
            total = op(total, val)
            if total in seen:
                print(total)
                return total
            seen.add(total)
    return "No repetitions found."


if __name__ == "__main__":
    do_part_1()
    do_part_2()
