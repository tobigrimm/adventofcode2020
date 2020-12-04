#!/usr/bin/env python3
import sys
import re
from typing import Dict

def check_passport(passport: Dict[str, str], deep_check: bool = False) -> bool:
    required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    optional_keys = ['cid']
    valid = len(set(required_keys).intersection(set(passport.keys()))) == len(required_keys)

    if deep_check and valid:
        checks = []
        """check the following fields
        
        
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.

    """
        checks.append(1920 <= int(passport['byr']) <= 2002)
        checks.append(2010 <= int(passport['iyr']) <= 2020)
        checks.append(2020 <= int(passport['eyr']) <= 2030)
        checks.append(passport['hgt'][-2:] in ['cm', 'in'] and (passport['hgt'][-2:] in "in" and int(passport['hgt'][:-2]) >= 59 and int(passport['hgt'][:-2])<=76) or (passport['hgt'][-2:] in "cm" and int(passport['hgt'][:-2]) >= 150 and int(passport['hgt'][:-2])<=193))
        checks.append(bool(re.match("#[0-9a-f]{6}", passport['hcl'])))
        checks.append(passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
        checks.append(len(passport['pid']) == 9)
        return all(checks)
    else:
        return valid
if __name__ == "__main__":
    with open(sys.argv[1], "r") as infile:
        passports = []
        passport: Dict[str, str] = {}
        for nextline in infile:
            line = nextline.strip().split()
            # check if new passport starts:
            if len(line) == 0:
                passports.append(passport)
                passport = {}
            else:
                for value in line:
                    k, v = value.strip().split(":")
                    passport[k] = v
    print("part 1: ", sum([check_passport(passport) for passport in passports]), " valid passports")
    print("part 2: ", sum([check_passport(passport, True) for passport in passports]), " valid passports")
