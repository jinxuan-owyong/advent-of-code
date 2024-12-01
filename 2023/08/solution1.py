# --- Day 8: Haunted Wasteland ---
import os
from typing import Dict, List, Tuple
DAY = "08"

# part 1


def processInput(data: List[str]) -> Tuple[str, Dict]:
    pattern, nodes = data[0].rstrip('\n'), [n.rstrip('\n') for n in data[2:]]
    edgeList = {}
    for n in nodes:
        name, branches = n.split(' = ')
        left, right = branches[1:-1].split(', ')
        edgeList[name] = {'L': left, 'R': right}
    return pattern, edgeList


def solve(document):
    pattern, edgeList = processInput(list(document))
    curr = 'AAA'
    count = 0
    while curr != 'ZZZ':
        for move in pattern:
            curr = edgeList[curr][move]
            count += 1
    print(count)


if __name__ == "__main__":
    with open(f"{os.getcwd()}/{DAY}/{input('Enter the input file id: ')}.input", "r") as document:
        solve(document)
