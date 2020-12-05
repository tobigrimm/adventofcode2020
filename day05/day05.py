#!/usr/bin/env python3
import sys
import re
from typing import Dict, List

def calculate_bsp(code: str, subrange: List[int]) -> List[int]:
    for char in code:
        if char == "F" or char == "L":
            subrange = subrange[:int(len(subrange)/2)]
        if char == "B" or char == "R":
            subrange = subrange[int(len(subrange)/2):]
    return subrange

def calculate_seat(seat: str) -> int:
    column = calculate_bsp(seat[:7], list(range(128)))[0]
    row = calculate_bsp(seat[7:], list(range(8)))[0]
    print(column, row)
    return (column*8 + row)


if __name__ == "__main__":
    with open(sys.argv[1], "r") as infile:
        seatcodes =[nextline.strip() for nextline in infile]
    print(
        "part 1: ",
        max([calculate_seat(seat) for seat in seatcodes]),
        " is the highest seat code",
    )
