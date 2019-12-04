from copy import copy

from day02.part1 import process_instructions
from helpers.input_utils import read_file

"""
"With terminology out of the way, we're ready to proceed.
To complete the gravity assist, you need to determine
what pair of inputs produces the output 19690720."

The inputs should still be provided to the program by
replacing the values at addresses 1 and 2, just like
before. In this program, the value placed in address
1 is called the noun, and the value placed in address
2 is called the verb. Each of the two input values
will be between 0 and 99, inclusive.

Once the program has halted, its output is available at
address 0, also just like before. Each time you try a
pair of inputs, make sure you first reset the computer's
memory to the values in the program (your puzzle input)
- in other words, don't reuse memory from a previous attempt.

Find the input noun and verb that cause the program
to produce the output 19690720. What is 100 * noun +
verb? (For example, if noun=12 and verb=2, the answer would
be 1202.)
"""


def calculate() -> int:
    line = read_file()
    str_codes = line.split(',')
    int_codes = [int(s) for s in str_codes]

    noun = -1
    verb = -1

    for x in range(0, 100):
        for j in range(0, 100):
            temp_copy = copy(int_codes)
            temp_copy[1] = x
            temp_copy[2] = j
            result = process_instructions(temp_copy)[0]

            if result == 19690720:
                noun = x
                verb = j
                break

    return 100 * noun + verb


if __name__ == '__main__':
    print(calculate())
