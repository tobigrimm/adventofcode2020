import math
import sys


if __name__ == "__main__":
    inputdata = open(sys.argv[1], "r").readlines()
    target = int(inputdata[0])
    buses = [int(bus) for bus in inputdata[1].strip().split(",") if bus != "x"]
    diff = [(int(target/bus)+1)*bus - target for bus in buses]
    min_diff = min(diff)
    print("Part 1:", buses[diff.index(min_diff)]*min_diff)

    buses = [(i,int(bus)) for i,bus in enumerate(inputdata[1].strip().split(",")) if bus != "x"]

    increase = 1
    t = 0

    # initially, I had the loop the otherway around and was checking each
    # increment (by 1) of the timestamp.
    # however, that is very slow, the other way around is basically instantaneous
    for dt, bus in buses:
        while True:
            if (dt+t)%bus == 0:
                break
            # start with increase 1 until the first bus loop is found,
            # then multiply the loop time to increase for each matching bus 
            t += increase
        # for each bus, add the loop time to increase
        increase *= bus

    print("Part 2:", t)
                

