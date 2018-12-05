#! /usr/bin/env python3

"""
Solve day 4
"""

from collections import defaultdict
from utils import input_lines


def get_guard_number_and_start(line):
    sline = line.split()
    return sline[3], int(sline[1][3:5])


def get_time(line):
    sline = line.split()
    return int(sline[1][3:5])


def time_sleeping(guard, guards):
    return sum(interval[1] - interval[0] for interval in guards[guard])


def most_common_time(guard, guards):
    time = None
    record = 0
    for i in range(60):
        irecord = 0
        for interval in guards[guard]:
            if interval[0] <= i and i < interval[1]:
                irecord += 1
        if irecord >= record:
            record = irecord
            time = i
    return time, record


def do_part_1():
    """
    Solves part 1
    """
    guards = defaultdict(list)

    lines = input_lines(4, test=False)
    guard, start = get_guard_number_and_start(lines[0])
    falls = None
    for line in lines[1:]:
        if 'asleep' in line:
            falls = get_time(line)
        elif 'wakes' in line:
            if falls:
                wakes = get_time(line)
                segment = [falls, wakes]
                falls = None
                guards[guard] = guards[guard] + [segment]
        elif '#' in line:
            if falls:
                wakes = get_guard_number_and_start(line)[1]
                if wakes < falls:
                    wakes = 60
                segment = [falls, wakes]
                falls = None
                guards[guard] = guards[guard] + [segment]
            segments_asleep = []
            guard, start = get_guard_number_and_start(line)

    max_time = 0
    max_guard_id = ""
    for guard in guards:
        time_slept = time_sleeping(guard, guards)
        if time_slept >= max_time:
            max_time = time_slept
            max_guard_id = guard
    time = most_common_time(max_guard_id, guards)[0]
    print(int(max_guard_id[1:]) * int(time))
    return guards


def do_part_2(guards):
    time = None
    record = 0
    maxguard = None
    for guard in guards:
        itime, irecord = most_common_time(guard, guards)
        if irecord >= record:
            record = irecord
            time = itime
            maxguard = guard
    print(int(time)*int(maxguard[1:]))
    return


if __name__ == "__main__":
    gds = do_part_1()
    do_part_2(gds)
