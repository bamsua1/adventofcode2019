from typing import Union

from helpers.input_utils import read_file


"""
Fuel required to launch a given module is based on its mass. Specifically,
to find the fuel required for a module,
take its mass, divide by three, round down, and subtract 2.

For example:

For a mass of 12, divide by 3 and round down to get 4,
then subtract 2 to get 2.
For a mass of 14, dividing by 3 and rounding down still yields 4,
so the fuel required is also 2.
For a mass of 1969, the fuel required is 654.
For a mass of 100756, the fuel required is 33583.
The Fuel Counter-Upper needs to know the total fuel requirement.
To find it, individually calculate the fuel
needed for the mass of each module (your puzzle input),
then add together all the fuel values.

What is the sum of the fuel requirements
for all of the modules on your spacecraft?
"""


def calculate() -> int:
    total = 0
    lines = read_file()
    for mass in lines.splitlines():
        total += (int(mass) // 3) - 2

    return total


def calculate_single(mass: Union[str, int]):
    return (int(mass) // 3) - 2


if __name__ == '__main__':
    print(calculate())
