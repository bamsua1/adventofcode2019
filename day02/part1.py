import pytest

from typing import List

from helpers.input_utils import read_file


def calculate() -> int:
    line = read_file()
    str_codes = line.split(',')
    int_codes = [int(s) for s in str_codes]
    int_codes[1] = 12
    int_codes[2] = 2
    return process_opcode(int_codes)[0]


def process_opcode(int_codes) -> List[int]:
    length = len(int_codes)
    for index in range(0, length, step=4):
        op_code = int_codes[index]
        op_index_one = int_codes[index + 1]
        op_index_two = int_codes[index + 2]
        result_position = int_codes[index + 3]

        if op_index_one > (length - 1) or op_index_two > (length - 1) or result_position > (length - 1):
            print('Some resulting index is greater than the length of array.')
            print(f'Length: {length}')
            print(f'Op index one: {op_index_one}; Op index two: {op_index_two}; Resulting index: {result_position}. ')
            exit(1)

        if op_code == 1:
            int_codes[result_position] = int_codes[op_index_one] + int_codes[op_index_two]
        elif op_code == 2:
            int_codes[result_position] = int_codes[op_index_one] * int_codes[op_index_two]
        elif op_code == 99:
            print('halting')
            break

    return int_codes


@pytest.mark.parametrize(
    ['input', 'expected'],
    [
        (
            [1, 0, 0, 0, 99], [2, 0, 0, 0, 99]
        )
    ]
)
def test_result(input, expected):
    assert process_opcode(int_codes=input) == expected


if __name__ == '__main__':
    assert process_opcode(int_codes=[1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    test_result()
    # print(calculate())
