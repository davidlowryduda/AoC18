#! /usr/bin/env python3

"""
Solve day 9
"""

from collections import deque
from utils import input_lines

def digest_line(line):
    """
    Returns number of players and last marble count.
    """
    sline = line.split()
    num_players, num_marble = sline[0], sline[6]
    return num_players, num_marble


def insert_marble(num, marble_deque):
    """
    Inserts marble into list per rules.

    Typically marbles are inserted at spot 2 to the right of the original. This
    amounts to rotating by 1 and appending.

    If 23 divides num, then this doesn't add a marble. Instead, the marble at
    spot index-7 is also removed, and the score becomes 23+(marble@index-7). The
    new index is at index-7 (which is a new marble).
    """
    if num % 23:
        marble_deque.rotate(-1)
        marble_deque.append(num)
        score = 0
    else:
        marble_deque.rotate(7)
        score = marble_deque.pop() + num
        marble_deque.rotate(-1)
    return score


def do_part_1(day, test=False):
    lines = input_lines(day, test=test)
    nplayers, nmarbles =map(int, digest_line(lines[0]))
    scores = [0] * nplayers
    marble_deque = deque([0])
    for marble in range(1, nmarbles):
        turn_score = insert_marble(marble, marble_deque)
        scores[marble % nplayers] += turn_score
        #print(marble_deque)
    print(max(scores))
    return


def do_part_2(day, test=False):
    lines = input_lines(day, test=test)
    nplayers, nmarbles =map(int, digest_line(lines[0]))
    nmarbles = nmarbles * 100
    scores = [0] * nplayers
    marble_deque = deque([0])
    for marble in range(1, nmarbles):
        turn_score = insert_marble(marble, marble_deque)
        scores[marble % nplayers] += turn_score
        #print(marble_deque)
    print(max(scores))
    return


if __name__ == "__main__":
    do_part_1(9, test=False)
    do_part_2(9, test=False)
