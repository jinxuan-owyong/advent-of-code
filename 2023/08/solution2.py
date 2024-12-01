# --- Day 8: Haunted Wasteland ---
import os
from typing import Dict, List, Tuple
import math
DAY = "08"

# part 2


def processInput(data: List[str]) -> Tuple[str, Dict[str, Dict], list]:
    pattern, nodes = data[0].rstrip('\n'), [n.rstrip('\n') for n in data[2:]]
    edgeList = {}
    for node in nodes:
        name, branches = node.split(' = ')
        left, right = branches[1:-1].split(', ')
        edgeList[name] = {'L': left, 'R': right}
    return pattern, edgeList, list(filter(lambda x: x[-1] == 'A', edgeList))


def solve(document):
    pattern, edgeList, startingNodes = processInput(list(document))
    count = 0
    stepsToZ = {}
    
    for node in startingNodes:
        curr = node
        count = 0
        while curr[-1] != 'Z':
            for move in pattern:
                curr = edgeList[curr][move]
                count += 1
        stepsToZ[curr] = count
    cycleCount = list(map(lambda x: x[1], stepsToZ.items()))
    print(math.lcm(*cycleCount))


if __name__ == "__main__":
    with open(f"{os.getcwd()}/{DAY}/{input('Enter the input file id: ')}.input", "r") as document:
        solve(document)
