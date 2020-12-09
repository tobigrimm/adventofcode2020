#!/usr/bin/env python3
import sys
import re
from itertools import islice, permutations

from typing import Any, List, Iterator, Generator
# from ..tools import sliding_window


def window(seq: Iterator[Any], n: int = 2) -> Generator[Any, None, None]:
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    "taken from https://docs.python.org/release/2.3.5/lib/itertools-example.html"
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


def check_sums(numbers: List[int], preamble_len: int) -> int:
    for *sublist, tail in window(numbers, preamble_len+1):
        results = [sum(perm) == tail for perm in permutations(sublist, 2)]
        if not any(results):
            return tail
    return -1

if __name__ == "__main__":
    preamble_len = int(sys.argv[2])
    with open(sys.argv[1], "r") as infile:
        numbers = []
        for nextline in infile:
            num = int(nextline.strip())
            numbers.append(num)
    print("Part 1:", check_sums(numbers, preamble_len), " is not the sum of the preceding %s numbers" % preamble_len)
    print("Part 2:")
