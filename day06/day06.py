#!/usr/bin/env python3
import sys
from typing import List, Set


def check_group(group: List[Set[str]], part1: bool = True) -> int:
    result = group[0]
    for s in group[1:]:
        if part1:
            result = result.union(s)
        else:
            result = result.intersection(s)
    return len(result)


if __name__ == "__main__":
    with open(sys.argv[1], "r") as infile:
        groups = []
        group: List[Set[str]] = []
        for nextline in infile:
            line = nextline.strip().split()
            # check if new passport starts:
            if len(line) == 0:
                groups.append(group)
                group = []
            else:
                for value in line:
                    group.append(set(value.strip()))
        # append the last passport after the last line
        groups.append(group)

    print(
        "part 1: ",
        sum([check_group(group) for group in groups]),
        " answered yes",
    )
    print(
        "part 2: ",
        sum([check_group(group, False) for group in groups]),
        " answered yes",
    )
