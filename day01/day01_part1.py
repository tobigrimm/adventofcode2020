#!/usr/bin/env python3
from typing import List, Tuple

def calc_2020(inlist: List[int]) -> Tuple[int, int]:
    return (0,0)




if __name__ == "__main__":

    with open("input", 'r') as infile:
        inlist = [line.strip() for line in infile]
    print(calc_2020(inlist))
