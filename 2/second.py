from typing import List


def get_input():
    with open('input') as f:
        lines = f.readlines()
        return lines


def parse_line(inp_line: str):
    s = inp_line.split(':')
    rule_part = s[0]
    password = s[1]
    password = password.strip()

    pos_first_to, char = rule_part.split(' ')

    pos_first, pos_second = pos_first_to.split('-')
    pos_first = int(pos_first)
    pos_second = int(pos_second)

    return pos_first, pos_second, char, password


def test_line(pos_first: int, pos_second: int, char: str, password: str):
    first_char = password[pos_first - 1]
    second_char = password[pos_second - 1]
    if f'{first_char}{second_char}'.count(char) == 1:
        return True
    return False


def check_lines(inp):
    valid_counter = 0
    for line in inp:
        parsed = parse_line(line)
        print(parsed)
        is_valid = test_line(*parsed)
        print(f'{line} is {is_valid}')
        if is_valid:
            valid_counter += 1
    return valid_counter


if __name__ == '__main__':
    inp = get_input()
    print(f'got {len(inp)} lines')
    valid_count = check_lines(inp)
    print(valid_count)
