#!/usr/bin/env python3
from typing import List, Tuple
from operator import mul
from functools import reduce
from itertools import combinations

def calc_2020(inlist: List[int]) -> Tuple[int, int]:
    """compare all numbers in inlist with each other.
       If the sum of two numbers results in 2020,
       return the first two numbers as a tuple"""
    return [(i, j) for i, j in combinations(inlist, 2) if i+j == 2020][0]




if __name__ == "__main__":

    with open("input", 'r') as infile:
        # important: input should contain no empty lines, otherwise the int() cast will fail
        inlist = [int(line.strip("\r\n").strip()) for line in infile]
    print("Product of the two numbers for day01 - part 1:", reduce(mul, calc_2020(inlist), 1))
