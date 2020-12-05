from typing import List


def get_input():
    with open('input') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        return lines


def row_to_binary(s: str):
    s = s.replace('F', '0')
    s = s.replace('B', '1')
    return int(s, 2)

def seat_to_binary(s: str):
    s = s.replace('R', '1')
    s = s.replace('L', '0')
    return int(s, 2)

def get_row_col(line):
    row_str = line[:7]
    seat_str = line[7:]
    row = row_to_binary(row_str)
    col = seat_to_binary(seat_str)
    return row, col

def get_id(row, col):
    return row * 8 + col

if __name__ == '__main__':
    inp = get_input()
    ids = []
    for line in inp:
        row, col = get_row_col(line)
        _id = get_id(row, col)
        ids.append(_id)
    ids.sort()
    this_id = ids.pop()
    while ids:
        next_id = ids.pop()
        if next_id - this_id != -1:
            print(this_id, next_id)
        this_id = next_id


