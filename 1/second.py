from typing import List


def get_input():
    with open('input') as f:
        lines = f.readlines()
        return lines


def get_numbers_2020(inp: List[int]):
    for idx_1, num_1 in enumerate(inp):
        for idx_2, num_2 in enumerate(inp):
            for idx_3, num_3 in enumerate(inp):
                if num_1 + num_2 + num_3 == 2020:
                    return True, num_1, num_2, num_3
    return False, 0, 0, 0

if __name__ == '__main__':
    inp = get_input()
    inp_numbers = [int(n) for n in inp]
    success, num_1, num_2, num_3 = get_numbers_2020(inp_numbers)
    if success:
        print(num_1 * num_2 * num_3)
    else:
        print('nope')

