#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Solve day 2.
"""

from collections import Counter
from utils import input_lines


def digest_line(line):
    """
    Parses a line into a dictionary containing letter counts.
    """
    seen = Counter(line.strip())
    return seen


def contains_nple(seen_dict, reps=2):
    """
    Returns True if line contains a letter exactly `reps` times.
    """
    if reps in seen_dict.values():
        return True
    return False


def do_part_1():
    """
    Solves part 1
    """
    digested_lines = list(map(digest_line, input_lines(2)))
    # Poor man's partial
    doubles = sum(map(lambda l: contains_nple(l, reps=2), digested_lines))
    triples = sum(map(lambda l: contains_nple(l, reps=3), digested_lines))
    print(doubles * triples)
    return doubles * triples


def distance(word1, word2):
    """
    Returns the number of different letters between word1 and word2
    """
    ndiffs = 0
    for a, b in zip(word1, word2):
        if a != b:
            ndiffs += 1
    return ndiffs


def common_substring(word1, word2):
    """
    Returns the common substring between word1 and word2
    """
    ret = ""
    for a, b in zip(word1, word2):
        if a == b:
            ret += a
    return ret


def do_part_2():
    """
    Solves part 2
    """
    lines = input_lines(2)
    for line1 in lines:
        for line2 in lines:
            if distance(line1, line2) == 1:
                common = common_substring(line1, line2)
                print(common)
                return common
    return ""


if __name__ == "__main__":
    do_part_1()
    do_part_2()
