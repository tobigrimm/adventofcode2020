#!/usr/bin/env python3
import sys
from collections import Counter, defaultdict
from typing import Tuple, List, Counter as TypeCounter



def check_neighbors(map, row_num, col_num, symbol) -> int:
    """return the number of symbols around the seat specified
        by row and col"""
    results = 0
  
    copy = map.keys()
    # print("neighbors:", row_num, col_num) 
    for row in range(row_num-1, row_num+2):
        for col in range(col_num-1,col_num+2):
            if (row, col) in copy:
                #print(row, col)
                # dont check the seat itself :)
                if map[(row, col)] == symbol:
                    if not (row, col) == (row_num, col_num):
                        results += 1
    # print("res:", results)
    return results




def calculate_step(map: List[List[str]]) -> Tuple[bool, List[List[str]]]:
    changes = [] 
    next_map = defaultdict(str)
    for entry in map.items():
        row_num, col_num = entry[0]
        seat = entry[1]
        next_seat = seat
        num_neighbors = check_neighbors(map, row_num, col_num, "#")
        if seat == "L":
            if num_neighbors == 0:
                next_seat = "#"
            else:
                pass
                #print("Empty seat will stay empty:", row_num, col_num, num_neighbors)

        if seat == "#" and num_neighbors >= 4:
            next_seat = "L"
        if next_seat != seat:
            changes.append(True)
            #print("Next: ", row_num, col_num, next_seat, num_neighbors)
        next_map[(row_num, col_num)] = next_seat
            
    return (any(changes), next_map)

if __name__ == "__main__":
    map = defaultdict(str)
    with open(sys.argv[1], "r") as infile:
        # add initial 0 as input jolt

        # TODO change all to defaultdict, use (row, col) as key!
        line = 0
        for nextline in infile:
            for num, char in enumerate(nextline.strip()):
                map[(line, num)] = char
            line += 1
   
    # print(map) 

    round = 0
    run = True
    while run:
        #print(check_neighbors(map, 9, 10, "#"))
        #print("Round: ", round, "\n Map: ", map)
        round += 1
        change, next_map = calculate_step(map)
        if change:
            map = next_map
        else:
            run = False
        #if round > 10:
        #    run = False
    print("Part1: ", list(map.values()).count("#"))
    #print("Part2: ", get_variants(jolts))
