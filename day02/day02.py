#!/usr/bin/env python3

import re

def check_policy(policy: str, password: str, mode: int = 1) -> bool:
    numbers, char = policy.split(" ")
    lower_bound, upper_bound = [int(num) for num in numbers.split("-")]

    if mode == 1:
        occ = password.count(char)
        return lower_bound <= occ <= upper_bound 
    else:
        # policy starts at place 1, not 0 in the string
        matches = [match.start()+1 for match in re.finditer(char, password)]
        return bool((lower_bound in matches) ^ (upper_bound in matches))

        
    

if __name__ == "__main__":
    with open("input", "r") as infile:
        check_lines = [line.strip().split(":") for line in infile]
    print("Valid passwords for part1:", sum([check_policy(policy.strip(), password.strip()) for policy, password in check_lines]))
    print("Valid passwords for part2:", sum([check_policy(policy.strip(), password.strip(), 2) for policy, password in check_lines]))
