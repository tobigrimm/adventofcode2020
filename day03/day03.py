#!/usr/bin/env python3
import sys
from typing import List


def navigate_slope(map: List, x_inc: int = 1, y_inc: int = 3) -> int:
    h = len(map)
    w = len(map[0])
    x, y = 0, 0
    trees = 0
    while x < h:
        if map[x][y] == "#":
            trees+=1
        x += x_inc
        # simulate the endless repeat to the right
        y = (y+y_inc) % w

    return trees



if __name__ == "__main__":
    with open(sys.argv[1], "r") as infile:
        map = [line.strip() for line in infile]
    print(f"part 1: {navigate_slope(map)} trees hit")
