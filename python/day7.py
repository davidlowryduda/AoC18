#! /usr/bin/env python3

"""
Solve day 7
"""

from collections import defaultdict
from utils import input_lines

def digest_line(line):
    """
    Lines are of the form

      Step A must be finished before step I can begin.

    Returns (A, I).
    """
    return (line[5], line[36])

def remove_pre(reqs, pre):
    for key in reqs:
        if pre in reqs[key]:
            reqs[key].remove(pre)
    return

def list_available(reqs, done):
    done = set(done)
    cands = list(set(reqs.keys()).union(*[set(val) for val in reqs.values()]).difference(done))
    available = []
    for key in cands:
        has_no_pres = True
        for possible in cands:
            if possible in reqs[key]:
                has_no_pres = False
        if has_no_pres:
            available += key
    return sorted(available)

def go_to_work(reqs, done, available, time_record, elapsed):
    currently = list(worker[1] for worker in time_record)
    for workernum in range(len(time_record)):
        worker = time_record[workernum]
        if worker and worker[0] <= 0:
            completed = worker[1]
            if completed:
                done += completed
                done = list(set(done))
                remove_pre(reqs, completed)
                available = list_available(reqs, done)
                worker = (0, '')
                time_record[workernum] = worker
                currently = list(w[1] for w in time_record)
            now_available = sorted(list(set(available).difference(set(currently))))
            if now_available:
                task = now_available[0]
                print("Starting {} at {}".format(task, elapsed))
                time = ord(task) - 4
                worker = (time, task)
                time_record[workernum] = worker
                currently = list(w[1] for w in time_record)
    # This is a lousy way of saying to check the whole list of workers again.
    # Otherwise, it could have been that worker 3 finished a task that would
    # have let the otherwise idle worker 1 work
    currently = list(worker[1] for worker in time_record)
    for workernum in range(len(time_record)):
        worker = time_record[workernum]
        if worker and worker[0] <= 0:
            completed = worker[1]
            if completed:
                done += completed
                done = list(set(done))
                remove_pre(reqs, completed)
                available = list_available(reqs, done)
                worker = (0, '')
                time_record[workernum] = worker
                currently = list(w[1] for w in time_record)
            now_available = sorted(list(set(available).difference(set(currently))))
            if now_available:
                task = now_available[0]
                print("Starting {} at {}".format(task, elapsed))
                time = ord(task) - 4
                worker = (time, task)
                time_record[workernum] = worker
                currently = list(w[1] for w in time_record)
    return time_record, reqs, done

def advance_time(time_record):
    for workernum in range(len(time_record)):
        worker = time_record[workernum]
        worker = (max(worker[0] - 1, 0), worker[1])
        time_record[workernum] = worker
    return

def do_part_1(test=False):
    lines = input_lines(7, test=test)
    reqs = defaultdict(set)
    done = []
    for line in lines:
        pre, task = digest_line(line)
        reqs[task].add(pre)
    available = list_available(reqs, done)
    while available:
        done += available[0]
        remove_pre(reqs, available[0])
        available = list_available(reqs, done)
    print(''.join(done))
    return


def do_part_2(test=False):
    elapsed = 0
    lines = input_lines(7, test=test)
    reqs = defaultdict(set)
    done = []
    time_record = 5*[(0, '')]
    for line in lines:
        pre, task = digest_line(line)
        reqs[task].add(pre)
    available = list_available(reqs, done)
    go_to_work(reqs, done, available, time_record, elapsed)
    while available and elapsed < 10000:
        advance_time(time_record)
        time_record, reqs, done = go_to_work(reqs, done, available, time_record, elapsed)
        available = list_available(reqs, done)
        elapsed += 1
    print(elapsed)
    return


if __name__ == "__main__":
    #do_part_1(test=False)
    do_part_2(test=False)
