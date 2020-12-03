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

    rule_from_to, char = rule_part.split(' ')

    rule_from, rule_to = rule_from_to.split('-')
    rule_from = int(rule_from)
    rule_to = int(rule_to)

    return rule_from, rule_to, char, password

def test_line(rule_from: int, rule_to: int, char: str, password: str):
    char_count = password.count(char)
    if rule_from <= char_count <= rule_to:
        return True
    return False

def check_lines(inp):
    valid_counter= 0
    for line in inp:
        parsed =  parse_line(line)
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

