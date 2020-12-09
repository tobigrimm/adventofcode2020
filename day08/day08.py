#!/usr/bin/env python3
import sys
import re
from typing import Any, List


def run_instructions(code: List[Any]) -> int:
    acc = 0
    eip = 0
    visited_instructions = []
    looped = False
    try:
        while eip < len(code):
            if eip in visited_instructions:
                looped = True
                break
            ins = code[eip]
            arg = code[eip+1]
            print(f"{eip}, {ins}, {arg}")
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
            eip = (eip+(next*2))
    except:
        print(err)
        pass
        
    return (looped, acc)

def mutate(code: List[Any]) -> int:
    for i, ins in enumerate(code):
        print(f"changing {i} ins: {ins}")
        mutated_code = code.copy()
        if ins == "nop":
            mutated_code[i] = "jmp"
        elif ins == "jmp":
            mutated_code[i] = "nop"
        print("changed", mutated_code[i], "complete code:", mutated_code)
        looped, acc = run_instructions(mutated_code)
        print(looped, acc)
        if not looped:
            print("not looped, acc:", acc)
            break

if __name__ == "__main__":
    with open(sys.argv[1], "r") as infile:
        machinecode = []
        for nextline in infile:
            ins, arg = nextline.strip().split(" ")
            machinecode.extend([ins, int(arg)])
    #print(machinecode)
    print("Part 1: Accumulator is: ", run_instructions(machinecode)[1])
    print("Part 2: Accumulator is: ", mutate(machinecode))
 
