#!/usr/bin/env python3
import sys
import re
from typing import Any, List


def run_instructions(code: List[Any]) -> int:
    acc = 0
    eip = 0
    visited_instructions = []
    while eip <= len(code):
        if eip in visited_instructions:
            break
        ins = code[eip]
        arg = code[eip+1]
        #print(f"{eip}, {ins}, {arg}")
        visited_instructions.append(eip)
        next = 1
        if ins == "nop":
            pass
        if ins == "acc":
            acc += arg
        if ins == "jmp":
            next = arg
        # TODO for later: check the arguments for the current instruction
        # next * 2 due to the argument after each instruction
        # TODO alternatively, put tuple of (ins, arg0, arg1, ..., argN) in the 
        #  list of codes for variable number of arguments?
        eip = (eip+(next*2))%len(code)

    return acc

if __name__ == "__main__":
    with open(sys.argv[1], "r") as infile:
        machinecode = []
        for nextline in infile:
            ins, arg = nextline.strip().split(" ")
            machinecode.extend([ins, int(arg)])
    #print(machinecode)
    print(run_instructions(machinecode))

    # print("Part 1: ", len(nx.ancestors(G, "shiny gold")))
    # # dont count the topmost shiny gold bag!
    # print("Part 2: ", count_bags(G, "shiny gold") - 1)
