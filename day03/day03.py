#!/usr/bin/env python3
import sys
from typing import List


def navigate_slope(map: List[str], x_inc: int = 1, y_inc: int = 3) -> int:
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
    part1 = navigate_slope(map)
    print(f"part 1: {part1} trees hit")
    result = 1
    # calculate the possible results
    for x,y in [(1,1), (1,3), (1,5), (1,7), (2,1)]:
        result *= navigate_slope(map, x, y)

    print(f"part 2: {result} trees hit")
    
