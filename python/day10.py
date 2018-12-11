#! /usr/bin/env python3

"""
Solve day 10
"""

from utils import input_lines
import re


def digest_line(line):
    num_re = re.compile("<(.*?)>")
    pos_data, vel_data = num_re.findall(line)
    posx, _, posy = pos_data.partition(',')
    velx, _, vely = vel_data.partition(',')
    posx, posy = int(posx), int(posy)
    velx, vely = int(velx), int(vely)
    return ((posx, posy), (velx, vely))


def centroid(positions):
    x = sum(pos[0] for pos in positions)/len(positions)
    y = sum(pos[1] for pos in positions)/len(positions)
    return int(x), int(y)


def print_portion(positions, xradius=40, yradius=10):
    centerx, centery = centroid(positions)
    for y in range(centery-yradius, centery+yradius):
        row = ''
        for x in range(centerx-xradius, centerx+xradius):
            if (x, y) in positions:
                row += '#'
            else:
                row += '.'
        print(row)
    return


def advance_time(positions, velocities, secs=1):
    for num in range(len(positions)):
        newx = positions[num][0] + secs * velocities[num][0]
        newy = positions[num][1] + secs * velocities[num][1]
        positions[num] = (newx, newy)
    return


def L1(positions):
    centerx, centery = centroid(positions)
    dist = 0
    for pos in positions:
        dist += abs(pos[0] - centerx) + abs(pos[1] - centery)
    return dist


def do_part_1(day, test=False):
    lines = input_lines(day, test=test)
    positions = []
    velocities = []
    for line in lines:
        pos_vector, vel_vector = digest_line(line)
        positions.append(pos_vector)
        velocities.append(vel_vector)
    L1_0 = L1(positions)
    advance_time(positions, velocities)
    L1_1 = L1(positions)
    diff = L1_0 - L1_1
    guess = int(L1_0 / diff)

    advance_time(positions, velocities, secs=guess)
    for i in range(20):
        print_portion(positions)
        print(L1(positions))
        # Added for part 2
        if L1(positions) == 6213:
            print(guess + 1 + i)
        advance_time(positions, velocities)

    return


def do_part_2(day, test=False):
    """
    Done in part 1 today.
    """
    return


if __name__ == "__main__":
    do_part_1(10, test=False)
    #do_part_2(10, test=False)
