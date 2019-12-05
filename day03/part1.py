from typing import List
from typing import Tuple

from shapely.geometry import LineString
from shapely.geometry import Point

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
    return closest_distance_to_starting(intersections)


def closest_distance_to_starting(intersections: List[Point]):
    distances = [manhattan_distance(STARTING_POINT, p) for p in intersections]
    return min(distances)


def manhattan_distance(point_a: Point, point_b: Point) -> int:
    return abs(point_a.x - point_b.x) + abs(point_a.y - point_b.y)


def construct_wire(instructions: List[str]) -> List[Tuple[Point, Point]]:
    current = STARTING_POINT
    path: List[Tuple[Point, Point]] = []
    for inst in instructions:
        letter = inst[0]
        distance = int(inst[1:])

        if letter == 'R':
            end = Point(current.x, current.y + distance)
        elif letter == 'L':
            end = Point(current.x, current.y - distance)
        elif letter == 'U':
            end = Point(current.x - distance, current.y)
        elif letter == 'D':
            end = Point(current.x + distance, current.y)
        else:
            print('bad value')
            return []

        path.append((current, end))
        current = end

    return path


def find_intersections(path_one: List[Tuple[Point, Point]],
                       path_two: List[Tuple[Point, Point]]) -> List[Point]:
    intersections = []
    for p in path_one:
        a = (p[0].x, p[0].y)
        b = (p[1].x, p[1].y)
        line_one = LineString([a, b])
        for j in path_two:
            a = (j[0].x, j[0].y)
            b = (j[1].x, j[1].y)
            line_two = LineString([a, b])

            int_pt = line_one.intersection(line_two)
            if int_pt:
                if int_pt.xy == STARTING_POINT.xy:
                    continue

                intersections.append(Point(int_pt.x, int_pt.y))

    return intersections


if __name__ == '__main__':
    print(calculate())
