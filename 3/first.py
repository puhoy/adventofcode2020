from typing import List


def get_input():
    with open('input') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        return lines


def hit_tree_at_index(line, x, width):
    x = x % (width)
    try:
        if line[x] == '#':
            print(line[:x] + 'X' + line[x + 1:])
            return True
        elif line[x] == '.':
            print(line[:x] + 'O' + line[x + 1:])
            return False
        else:
            print('something unexpected')
            print(f'input line {x}: "{inp[x]}"')

    except Exception as e:
        print(f'error at {x}')
        print(f'line {line}')
        raise
    exit(1)


def traverse(inp):
    height = len(inp)
    width = len(inp[0])
    print(f'width {width}, height {height}')
    x = 0
    trees_hit = 0
    for num, line in enumerate(inp):
        if hit_tree_at_index(line, x, width):
            trees_hit += 1
        x += 3
    print(trees_hit)


if __name__ == '__main__':
    inp = get_input()
    traverse(inp)
