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
    Returns file to input for `day`.

    The input is assumed to be in `inputs/input<day>.txt`, where <day> is
    replaced with the number of the day.

    Note that it's likely that `read_input(<day>).read()` will be called.
    """
    return _read_file("inputs/input{}.txt".format(day))
