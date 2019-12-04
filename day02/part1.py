from typing import List

from helpers.input_utils import read_file

"""
An Intcode program is a list of integers separated by commas (like 1,0,0,3,99).
To run one, start by looking at the first integer (called position 0).
Here, you will find an opcode - either 1, 2, or 99. The opcode indicates
what to do;
for example, 99 means that the program is finished and should immediately halt.
Encountering an unknown opcode means something went wrong.

Opcode 1 adds together numbers read from two positions and stores
the result in a third position. The three integers immediately after
the opcode tell you these three positions - the first two indicate the
positions from which you should read the input values, and the third
indicates the position at which the output should be stored.

For example, if your Intcode computer encounters 1,10,20,30,
it should read the values at positions 10 and 20, add those values,
and then overwrite the value at position 30 with their sum.

Opcode 2 works exactly like opcode 1, except it multiplies the
two inputs instead of adding them. Again, the three integers
after the opcode indicate where the inputs and outputs are,
not their values.

Once you're done processing an opcode, move to
the next one by stepping forward 4 positions.

For example, suppose you have the following program:

1,9,10,3,2,3,11,0,99,30,40,50
For the purposes of illustration, here is the same
program split into multiple lines:

1,9,10,3,
2,3,11,0,
99,
30,40,50
The first four integers, 1,9,10,3, are at positions
0, 1, 2, and 3. Together, they represent the first opcode
(1, addition), the positions of the two inputs (9 and 10),
and the position of the output (3). To handle this opcode,
you first need to get the values at the input positions:
position 9 contains 30, and position 10 contains 40.
Add these numbers together to get 70. Then, store this
value at the output position; here, the output position
(3) is at position 3, so it overwrites itself.
Afterward, the program looks like this:

1,9,10,70,
2,3,11,0,
99,
30,40,50
Step forward 4 positions to reach the next opcode, 2.
This opcode works just like the previous, but it
multiplies instead of adding. The inputs
are at positions 3 and 11; these positions
contain 70 and 50 respectively. Multiplying
these produces 3500; this is stored at position 0:

3500,9,10,70,
2,3,11,0,
99,
30,40,50
Stepping forward 4 more positions arrives at opcode 99, halting the program.
"""


def calculate() -> int:
    line = read_file()
    str_codes = line.split(',')
    int_codes = [int(s) for s in str_codes]
    int_codes[1] = 12
    int_codes[2] = 2
    return process_instructions(int_codes)[0]


def process_instructions(int_codes) -> List[int]:
    length = len(int_codes)
    for address in range(0, length, 4):
        instruction = int_codes[address]
        if instruction == 99:
            break

        parameter_one = int_codes[address + 1]
        parameter_two = int_codes[address + 2]
        result_parameter = int_codes[address + 3]

        if (
                parameter_one > (length - 1) or
                parameter_two > (length - 1) or
                result_parameter > (length - 1)
        ):
            print('Some resulting index is greater than '
                  'the length of array.')
            print(f'Length: {length}')
            print(
                f'Op index one: {parameter_one}; '
                f'Op index two: {parameter_two}; '
                f'Resulting index: {result_parameter}. '
            )
            exit(1)

        if instruction == 1:
            int_codes[result_parameter] = (int_codes[parameter_one] +
                                           int_codes[parameter_two])
        elif instruction == 2:
            int_codes[result_parameter] = (int_codes[parameter_one] *
                                           int_codes[parameter_two])

    return int_codes


if __name__ == '__main__':
    print(calculate())
