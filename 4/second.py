from typing import List
import re


def get_input():
    with open('input') as f:
        lines = f.readlines()
        return lines


class InvalidPassportException(Exception):
    pass


class Passport:
    def __init__(self, passport_dict):
        self.passport_dict = passport_dict

        self.byr = int(passport_dict['byr'])
        self.iyr = int(passport_dict['iyr'])
        self.eyr = int(passport_dict['eyr'])
        self.hgt = passport_dict['hgt']
        self.hcl = passport_dict['hcl']
        self.ecl = passport_dict['ecl']
        self.pid = passport_dict['pid']
        self.cid = passport_dict.get('cid', True)

        self.validate()

    def validate(self):
        if not 1920 <= self.byr <= 2002:
            raise InvalidPassportException
        if not 2010 <= self.iyr <= 2020:
            raise InvalidPassportException
        if not 2020 <= self.eyr <= 2030:
            raise InvalidPassportException

        # check height
        try:
            height = int(self.hgt[:-2])
        except ValueError:
            raise InvalidPassportException
        unit = self.hgt[-2:]
        if unit == 'cm':
            if not 150 <= height <= 193:
                raise InvalidPassportException
        elif unit == 'in':
            if not 59 <= height <= 76:
                raise InvalidPassportException
        else:
            print(f'unknown unit {unit}')
            print(self.passport_dict)
            raise InvalidPassportException

        # check hair color
        # "#123aff"
        if not self.hcl.startswith('#'):
            raise InvalidPassportException

        color = self.hcl[1:]
        if len(color) != 6:
            raise InvalidPassportException

        # find everything not 0-9a-f
        find_invalid_hair_chars = re.compile(r'[^a-f0-9]').search
        if find_invalid_hair_chars(color):
            raise InvalidPassportException

        if self.ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            raise InvalidPassportException

        if len(self.pid) != 9:
            raise InvalidPassportException
        find_invalid_pid_chars = re.compile(r'[^0-9]').search
        if find_invalid_pid_chars(self.pid):
            raise InvalidPassportException


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
        except InvalidPassportException as e:
            print(f'invalid passport after validation {passport_dict}')
            print(e)
    print(valid_passports)
