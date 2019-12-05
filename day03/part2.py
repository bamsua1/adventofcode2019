from math import sqrt
from typing import List
from typing import Tuple

from shapely.geometry import Point

from day03.part1 import construct_wire
from day03.part1 import find_intersections
from helpers.input_utils import read_file

STARTING_POINT = Point(8, 1)

"""
https://adventofcode.com/2019/day/3
"""


def calculate():
    lines = read_file()
    wires = lines.splitlines()
    path_one = construct_wire(wires[0].split(','))
    path_two = construct_wire(wires[1].split(','))

    intersections = find_intersections(path_one, path_two)
    steps = []
    for intersection in intersections:
        steps_one = find_num_of_steps(path_one, intersection)
        steps_two = find_num_of_steps(path_two, intersection)
        steps.append(steps_one + steps_two)

    return min(steps)


def find_num_of_steps(path: List[Tuple[Point, Point]],
                      intersection: Point) -> int:
    steps = 0
    for p in path:
        is_b = is_between(p[0], intersection, p[1])
        if is_b:
            steps += distance_between_two_points(p[0], intersection)
            break
        else:
            steps += distance_between_two_points(p[0], p[1])

    return steps


def distance_between_two_points(a: Point, b: Point):
    return sqrt((a.x - b.x)**2 + (a.y - b.y)**2)


def is_between(a: Point, c: Point, b: Point):
    """
    Check point c is inbetween points a & b
    :param a:
    :param c:
    :param b:
    :return:
    """
    return (
        distance_between_two_points(a, c) +
        distance_between_two_points(c, b) ==
        distance_between_two_points(a, b)
    )


if __name__ == '__main__':
    print(calculate())
