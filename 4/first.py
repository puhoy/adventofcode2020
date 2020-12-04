from typing import List


def get_input():
    with open('input') as f:
        lines = f.readlines()
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

    def parse_passport_strings(passport_data: [str]):
        """
        parses strings of a single passport

        eg
        ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
        byr:1937 iyr:2017 cid:147 hgt:183cm
        """
        passport_dict = {}
        for line in passport_data:
            for element in line.split(' '):
                key, value = element.split(':')
                passport_dict[key] = value
        return passport_dict


def get_passport_lines(inp):
    passports = []
    current_passport = []
    for line in inp:
        line = line.strip()
        if not line:
            passports.append(current_passport[:])
            current_passport = []
        else:
            current_passport.append(line)
    
    passports.append(current_passport[:])
    return passports

if __name__ == '__main__':
    inp = get_input()
    
    valid_passports = 0

    passports_raw = get_passport_lines(inp)
    for passport_data in passports_raw:
        passport_dict = Passport.parse_passport_strings(passport_data)
        try:
            passport = Passport(passport_dict)
            valid_passports += 1
            print(passport_dict)
        except KeyError as e:
            print(f'invalid passport {passport_dict}')
            print(e)
    print(valid_passports)
