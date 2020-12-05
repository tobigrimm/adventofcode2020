#!/usr/bin/env python3
import sys
import re
from typing import Dict, List, Iterator, Generator, Any 
from itertools import islice

def calculate_bsp(code: str, subrange: List[int]) -> List[int]:
    for char in code:
        if char == "F" or char == "L":
            subrange = subrange[: int(len(subrange) / 2)]
        if char == "B" or char == "R":
            subrange = subrange[int(len(subrange) / 2) :]
    return subrange

def window(seq: Iterator[Any], n: int =2) -> Generator[Any, None, None]:
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

def calculate_seat(seat: str) -> int:
    column = calculate_bsp(seat[:7], list(range(128)))[0]
    row = calculate_bsp(seat[7:], list(range(8)))[0]
    return column * 8 + row


if __name__ == "__main__":
    with open(sys.argv[1], "r") as infile:
        seatcodes = [nextline.strip() for nextline in infile]
    all_seats = sorted([calculate_seat(seat) for seat in seatcodes])
    print(
        "part 1: ",
        max(all_seats),
        " is the highest seat code",
    )
    for i,j,k in window(all_seats, 3):
        if i == j-1 and j+1 == k:
            pass
        else:
            if j+1 != k:
                missing_seat  = j+1
    print(
        "part 2: ",
        missing_seat,
        " is missing in the seat codes",
    )
