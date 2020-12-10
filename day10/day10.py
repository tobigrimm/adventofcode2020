#!/usr/bin/env python3
import sys
from collections import Counter, defaultdict
from typing import List, Counter as TypeCounter


def calculate_diffs(inlist: List[int]) -> int:
    result: TypeCounter[int] = Counter()
    jolt = 0
    dist = 0
    for i in inlist:

        diff = i - jolt
        if diff == 1:
            dist += 1
            result[diff] += 1
        jolt = i

    # add final 3 jolt jump
    result[3] += 1
    return int(result[1] * result[3])


def get_variants(inlist: List[int]) -> int:
    # defaultdict from int will default to 0 if an entry does not exist
    ways = defaultdict(int)
    ways[0] = 1
    # skip the leading 0, as that is always reached
    # and already account for above :)
    for i in inlist[1:]:
        ways[i] = ways[i - 1] + ways[i - 2] + ways[i - 3]
    return ways[max(inlist)]


if __name__ == "__main__":
    with open(sys.argv[1], "r") as infile:
        # add initial 0 as input jolt
        jolts = [0]
        for nextline in infile:
            jolt = int(nextline.strip())
            jolts.append(jolt)
    jolts = sorted(jolts)
    part1 = calculate_diffs(jolts)
    print("Part1: ", part1)
    print("Part2: ", get_variants(jolts))
