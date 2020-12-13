#!/usr/bin/env python3
import sys
from collections import Counter, defaultdict
from operator import add
from typing import Tuple, List, Counter as TypeCounter
import numpy as np
from enum import Enum
import math

class Compass(Enum):
    NORTH = (1,0) # np.array([1, 0])
    EAST = (0,1) #np.array([0, 1])
    SOUTH = (-1, 0 ) #np.array([-1, 0])
    WEST = (0, -1) #np.array([0, -1])

def calculate_distance(directions: List[str]):
    """move the ship along the calculated direction
        
            N:  (1,0)
            E:  (0,1)
            S:  (-1,0)
            W:  (0,-1)

    
    """


    dirmap = [np.array([1,0]), np.array((0,1)), np.array((-1,0)), np.array((0, -1))]
    location = np.array([0,0])
    facing = 1
    for dir in directions:
        steps = int(dir[1:])
        dir = dir[0]
        if dir == "F":
            location = location + dirmap[facing] * steps
        if dir == "N":
            location = location + np.array((1,0))* steps
        if dir == "E":
            location = location + np.array((0,1))* steps
        if dir == "S":
            location = location + np.array((-1,0))* steps
        if dir == "W":
            location = location + np.array((0,-1))* steps
        if dir == "R":
            facing = int((facing + steps/90) % 4)
        if dir == "L":
            facing = int((facing - steps/90) % 4)


    return location
            
def calculate_distance2(directions: List[str]):
    """move the ship along the calculated direction
        
            N:  (1,0)
            E:  (0,1)
            S:  (-1,0)
            W:  (0,-1)

    
    """


    dirmap = [np.array([1,0]), np.array((0,1)), np.array((-1,0)), np.array((0, -1))]
    location = np.array([0,0])
    #initial waypoint is 10 east and 1 north
    waypoint = np.array((1, 10))
    facing = 1
    for dir in directions:
        steps = int(dir[1:])
        dir = dir[0]
        if dir == "F":
            location = location + waypoint * steps
        if dir == "N":
            waypoint = waypoint + np.array((1,0))* steps
        if dir == "E":
            waypoint = waypoint + np.array((0,1))* steps
        if dir == "S":
            waypoint = waypoint + np.array((-1,0))* steps
        if dir == "W":
            waypoint = waypoint + np.array((0,-1))* steps
        if dir in ["R", "L"]:
            if dir == "L":
                steps = steps * -1
            waypoint = np.array((waypoint[0] * int(math.cos(math.radians(-steps))) + waypoint[1] * int(math.sin(math.radians(-steps))), waypoint[1] * int(math.cos(math.radians(-steps))) - waypoint[0] * int(math.sin(math.radians(-steps)))))


        print(location, waypoint)
    return location

if __name__ == "__main__":
    with open(sys.argv[1], "r") as infile:
        directions = [nextline.strip() for nextline in infile]

    part1 = calculate_distance(directions)
    print(part1)
    print("Part1: ", abs(part1[0])+abs(part1[1]))
    part2 = calculate_distance2(directions)
    print(part2)
    print("Part2: ", abs(part2[0])+abs(part2[1]))
    #print("Part2: ", part2)
