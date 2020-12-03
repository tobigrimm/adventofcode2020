#!/usr/bin/env python3
import sys


if __name__ == "__main__":
    with open(sys.argv[1], "r") as infile:
        map = [line.strip() for line in infile]

    h = len(map)
    w = len(map[0])
    x, y = 0, 0
    trees = 0
    while x < h:
        if map[x][y] == "#":
            print(x,y,h,w)
            trees+=1
        x += 1
        # simulate the endless repeat to the right
        y = (y+3) % w

    print(trees)
