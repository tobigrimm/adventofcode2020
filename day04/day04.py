#!/usr/bin/env python3
import sys
from typing import List


def check_passport(passport: dict) -> bool:
    required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    optional_keys = ['cid']
    return len(set(required_keys).intersection(set(passport.keys()))) == len(required_keys)

if __name__ == "__main__":
    with open(sys.argv[1], "r") as infile:
        passports = []
        passport = {}
        for line in infile:
            line = line.strip().split()
            # check if new passport starts:
            if len(line) == 0:
                passports.append(passport)
                print(passport)
                passport = {}
            else:
                for value in line:
                    k, v = value.strip().split(":")
                    passport[k] = v
        #passports = [[dict(values.split(":")) for values in entr ]for entry in [line.strip().split() for line in infile]]
        #print(passports)
        #passports2 = [dict(entry.split(":")) for passport in passports]
    print(passports)
    for passport in passports:
        print(check_passport(passport))
    print(sum([check_passport(passport) for passport in passports]))
    #print(f"part 1: {part1} trees hit")
    #result = 1
    # calculate the possible results
    #for x, y in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
    #    result *= navigate_slope(map, x, y)

    #print(f"part 2: {result} trees hit")
