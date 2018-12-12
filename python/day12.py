#! /usr/bin/env python3

"""
Solve day 12
"""

from utils import input_lines


def initial_setup(lines):
    """
    Extract the initial state and the rules.
    """
    init_state = lines[0].split()[-1]
    lines = lines[2:]
    rules = create_rules(lines)
    return init_state, rules


def create_rules(lines):
    """
    Given the list of line rules, create the rules dictionary.
    """
    rules = dict()
    for line in lines:
        sline = line.split()
        rules[sline[0]] = sline[-1]
    return rules


def evolve_state(state, rules):
    """
    Given state string, return a state string after applying rules.
    """
    ret = ''
    offsets = list(range(-2, 2 + 1))
    for index, symbol in enumerate(state[2:-2], 2):
        nbhood = ''.join(state[(index + offset)] for offset in offsets)
        ret += rules[nbhood]
    return '..' + ret + '..'


def sum_pots(state, leftpad=10):
    """
    Sum the pots with a '#' in them, assuming that pot 0 is at index 'leftpad'.
    """
    ret = 0
    for index, symbol in enumerate(state, -leftpad):
        if symbol == '#':
            ret += index
    return ret


def do_part_1(day, test=False):
    LEFTPAD = 10
    RIGHTPAD = 30
    lines = input_lines(day, test=test)
    init_state, rules = initial_setup(lines)
    # pad the initial state
    init_state = '.' * LEFTPAD + init_state + '.' * RIGHTPAD
    print(' ' * LEFTPAD + '0')
    print(init_state)
    state = init_state
    for i in range(20):
        state = evolve_state(state, rules)
        print(state)
    print(sum_pots(state, leftpad=LEFTPAD))
    return


def sum_potlist_after_time(potlist, time, init_time):
    return sum(map(lambda x: x + time - init_time, potlist))


def do_part_2(day, test=False):
    LEFTPAD = 10
    RIGHTPAD = 300
    lines = input_lines(day, test=test)
    init_state, rules = initial_setup(lines)
    # pad the initial state
    init_state = '.' * LEFTPAD + init_state + '.' * RIGHTPAD
    print(' ' * LEFTPAD + '0')
    print('  0', init_state[:150])
    state = init_state
    for i in range(119):
        state = evolve_state(state, rules)
        if '################' in state:
            rem = i+1
        #print(state[:180])
    #print(rem)
    first_trivial_state = evolve_state(state, rules) # Generation 120
    potlist = []
    for index, symbol in enumerate(first_trivial_state, -LEFTPAD):
        if symbol == '#':
            potlist.append(index)
    print(sum_potlist_after_time(potlist, 50000000000, 120))
    return


if __name__ == "__main__":
    do_part_1(12, test=False)
    do_part_2(12, test=False)
