from typing import List


def get_input():
    with open('input') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        return lines


class Passport:
    def __init__(self, passport_dict):
        self.byr = passport_dict['byr']
        self.iyr = passport_dict['iyr']
        self.eyr = passport_dict['eyr']
        self.hgt = passport_dict['hgt']
        self.hcl = passport_dict['hcl']
        self.ecl = passport_dict['ecl']
        self.pid = passport_dict['pid']
        self.cid = passport_dict.get('cid', True)


def merge_answer_groups(answer_groups_raw: [str]) -> List[set]:
    """
    only answers everybody in that group had
    eg:
    a
    ab
    => {a}
    """
    answers = []
    for group in answer_groups_raw:
        joined_answers = set(list(group.pop()))
        for line in group:
            joined_answers = joined_answers.intersection(set(list(line)))
        answers.append(joined_answers)
    return answers


def get_answer_lines(inp):
    answers = []
    current_answer_group = []
    for line in inp:
        line = line.strip()
        if not line:
            answers.append(current_answer_group[:])
            current_answer_group = []
        else:
            current_answer_group.append(line)

    answers.append(current_answer_group[:])
    return answers

def answer_sum(answer_groups):
    s = 0
    for answer in answer_groups:
        s += len(answer)
    return s


if __name__ == '__main__':
    inp = get_input()
    answer_groups_raw = get_answer_lines(inp)
    answer_groups = merge_answer_groups(answer_groups_raw)
    print(answer_groups) 
    print(answer_sum(answer_groups))


