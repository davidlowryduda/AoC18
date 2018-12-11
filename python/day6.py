#! /usr/bin/env python3

"""
Solve day 6
"""

from collections import defaultdict
from utils import input_lines


def digest_line(line, name):
    """
    Interprets a line of input to a point-tuple.
    """
    x, _, y = line.partition(",")
    x = int(x.strip())
    y = int(y.strip())
    return (x, y, name)


def bounding_box(ptlist):
    """
    Returns the bounding box for the list of points, in the form
    (x1, y1, x2, y2), where (x1, y1) is the top left of the box and
    (x2, y2) is the bottom right of the box.
    """
    xs = [pt[0] for pt in ptlist]
    ys = [pt[1] for pt in ptlist]
    return (min(xs), max(ys), max(xs), min(ys))


def nearest_pt(pt, ptlist):
    """
    Returns the point in pointlist nearest to pt, or '.' if there is a tie.
    """
    tie = False
    min_distance = 1000
    cand_pt = ''
    for q in ptlist:
        cand_distance = distance(pt, q)
        if cand_distance < min_distance:
            min_distance = cand_distance
            cand_pt = q
            tie = False
        elif cand_distance == min_distance:
            tie = True
    if tie:
        return '.'
    return cand_pt[2]


def distance(pt1, pt2):
    """
    Returns Manhattan distance between two points.

    A point is a tuple (x, y, name).
    """
    return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])


def do_part_1(test=False):
    lines = input_lines(6, test=test)
    pts = []
    for num, line in enumerate(lines):
        pts.append(digest_line(line, num))
    xmin, ymax, xmax, ymin = bounding_box(pts)
    #for y in range(ymin, ymax+1):
    #    print(''.join(str(nearest_pt((x,y), pts)) for x in range(xmin, xmax+1)))

    infinites = set()
    for y in range(ymin, ymax+1):
        _pt = (xmin, y)
        infinites.add(nearest_pt(_pt, pts))
    for y in range(ymin, ymax+1):
        _pt = (xmax, y)
        infinites.add(nearest_pt(_pt, pts))
    for x in range(xmin, xmax+1):
        _pt = (x, ymin)
        infinites.add(nearest_pt(_pt, pts))
    for x in range(xmin, xmax+1):
        _pt = (x, ymax)
        infinites.add(nearest_pt(_pt, pts))
    #print(infinites)

    tallies = defaultdict(int)
    for x in range(xmin, xmax+1):
        for y in range(ymin, ymax+1):
            _pt = (x, y)
            tallies[nearest_pt(_pt, pts)] += 1

    finites = [value for key, value in tallies.items() if key not in infinites]
    print(max(finites))
    return


def do_part_2(test=False):
    lines = input_lines(6, test=test)
    pts = []
    for num, line in enumerate(lines):
        pts.append(digest_line(line, num))
    xmin, ymax, xmax, ymin = bounding_box(pts)

    counter = 0
    for x in range(xmin, xmax + 1):
        for y in range(ymin, ymax + 1):
            _pt = (x, y)
            total = sum(distance(_pt, q) for q in pts)
            if total < 10000:
                counter += 1
    print(counter)
    return


if __name__ == "__main__":
    do_part_1(test=False)
    do_part_2(test=False)
