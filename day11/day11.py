#!/usr/bin/env python3
import sys
from collections import Counter, defaultdict
from operator import add
from typing import Tuple, List, Counter as TypeCounter



def check_neighbors(seatmap, row_num: int, col_num: int, symbol: str, direct: bool = True) -> int:
    """return the number of symbols around the seat specified
        by row and col"""
    results = 0
 
    
    copy = seatmap.keys()
    if not direct:
        for row in range(row_num-1, row_num+2):
            for col in range(col_num-1,col_num+2):
                if (row, col) in copy:
                    # dont check the seat itself :)
                    if seatmap[(row, col)] == symbol:
                        if not (row, col) == (row_num, col_num):
                            results += 1
        # print("res:", results)
    else:
        #build direction vectors:
        for dir in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            check_key = tuple(map(add, (row_num, col_num), dir))
            while check_key in copy:
                if seatmap[check_key] == symbol:
                    results += 1
                    break
                # stop looking if theres an empty seat
                elif seatmap[check_key] == "L":
                    break

                check_key = tuple(map(add, check_key, dir))

    # check if im being stupid :)
    assert(results <= 8)
    return results




def calculate_step(seatmap: List[List[str]], lim: int = 4, direct: bool = True) -> Tuple[bool, List[List[str]]]:
    changes = [] 
    next_seatmap = defaultdict(str)
    for entry in seatmap.items():
        row_num, col_num = entry[0]
        seat = entry[1]
        next_seat = seat
        num_neighbors = check_neighbors(seatmap, row_num, col_num, "#", direct)
        if seat == "L":
            if num_neighbors == 0:
                next_seat = "#"
            else:
                pass

        if seat == "#" and num_neighbors >= lim:
            next_seat = "L"
        if next_seat != seat:
            changes.append(True)
        next_seatmap[(row_num, col_num)] = next_seat
            
    return (any(changes), next_seatmap)

def calculate_rounds(seatmap, lim: int = 4, direct = False) -> int:
    round = 0
    run = True
    while run:
        round += 1
        change, next_seatmap = calculate_step(seatmap, lim, direct)
        if change:
            seatmap = next_seatmap
        else:
            run = False
    return list(seatmap.values()).count("#")

def print_nice_map(seatmap):
    result = ""
    for row in range(0,100):
        for col in range(0,100):
            if (row, col) in seatmap:
                result += str(seatmap[(row, col)])
        if (row, 0) in seatmap:
            result += "\n"
    return result

if __name__ == "__main__":
    seatmap = defaultdict(str)
    with open(sys.argv[1], "r") as infile:

        line = 0
        for nextline in infile:
            for num, char in enumerate(nextline.strip()):
                seatmap[(line, num)] = char
            line += 1
   

    part1 = calculate_rounds(seatmap.copy())
    print("Part1: ", part1)
    part2 = calculate_rounds(seatmap.copy(), 5, True)
    print("Part2: ", part2)
