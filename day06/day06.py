#!/usr/bin/env python3
import sys
import re
from typing import Dict

def len_group_yes(group: str) -> int:
    return len(set(group))

if __name__ == "__main__":
    with open(sys.argv[1], "r") as infile:
        groups = []
        group = ""
        for nextline in infile:
            line = nextline.strip().split()
            # check if new passport starts:
            if len(line) == 0:
                groups.append(group)
                group = ""
            else:
                for value in line:
                    group += value.strip()
        #append the last passport after the last line
        groups.append(group)
    
    
    print(
        "part 1: ",
        sum([len_group_yes(group) for group in groups]),
        " answered yes",
    )
    # print(
    #     "part 2: ",
    #     sum([check_passport(passport, True) for passport in passports]),
    #     " valid passports",
    # )
