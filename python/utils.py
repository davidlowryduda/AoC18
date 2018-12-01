#! /usr/bin/env python3
"""
utils.py --- Common utilities

Opens files, maybe does little math things, whatnot.
"""


def _read_file(filename):
    try:
        return open(filename, "r")
    except FileNotFoundError:
        print("The file was not found.")
        raise


def read_input(day):
    """
    Returns file of input for `day`.

    The input is assumed to be in `inputs/input<day>.txt`, where <day> is
    replaced with the number of the day.

    Note that it's likely that `read_input(<day>).read()` will be called.
    """
    return _read_file("inputs/input{}.txt".format(day))


def input_lines(day):
    """
    Saves the inputfile from day `day` line-by-line, stripping linebreaks.
    """
    return list(map(lambda x: x.strip(), read_input(day).readlines()))
