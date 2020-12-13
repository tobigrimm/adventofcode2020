import math
import sys


if __name__ == "__main__":
    inputdata = open(sys.argv[1], "r").readlines()
    target = int(inputdata[0])
    buses = [int(bus) for bus in inputdata[1].strip().split(",") if bus != "x"]
    diff = [(int(target/bus)+1)*bus - target for bus in buses]
    min_diff = min(diff)
    print("Part 1:", buses[diff.index(min_diff)]*min_diff)
