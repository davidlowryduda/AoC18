#! /usr/bin/env python3

"""
Solve day 5
"""

from utils import input_lines


def are_same(let1, let2):
    return ord(let1) - ord(let2) == 32 or ord(let2) - ord(let1) == 32

def collapse_once(s):
    s = s + '0'
    out = ''
    i = 0
    while i < len(s) - 1:
        a = s[i]
        b = s[i+1]
        if not are_same(a, b):
            out += a
            i = i + 1
        else:
            i = i + 2
    return out

def collapse_maximally(line):
    cline = collapse_once(line)
    while (cline != line):
        line = cline
        cline = collapse_once(cline)
    return cline

def remove_pair(ins, a):
    A = chr(ord(a) - 32)
    return ''.join(l for l in ins if (l != a) and (l != A))

def do_part_1(test=False):
    lines = input_lines(5, test=test)
    line = lines[0].strip()  # This challenge has only one line
    print(len(collapse_maximally(line)))
    return


def do_part_2(test=False):
    lines = input_lines(5, test=test)
    line = lines[0].strip()  # This challenge has only one line
    record = 9999999
    for letter in "abcdefghijklmnopqrstuvwxyz":
        col = collapse_maximally(remove_pair(line, letter))
        irec = len(collapse_maximally(remove_pair(line, letter)))
        print(letter, irec)
        if irec < record:
            record = irec
    print(record)
    return


if __name__ == "__main__":
    do_part_1()
    do_part_2()
