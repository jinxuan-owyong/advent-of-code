# --- Day 11: Cosmic Expansion ---
import os
from typing import List, Set, Tuple
import numpy as np
DAY = "11"

# part 2


# returns all positions matching #
def findGalaxyPositions(galaxy: np.ndarray) -> List[Tuple]:
    result = []
    for i, row in enumerate(galaxy):
        for j, cell in enumerate(row):
            if cell == '#':
                result.append((i, j))
    return result


# adds extra 1000000 if path taken goes through expanded rows/cols
def getGalaxyDistance(emptyRows: Set, emptyCols: Set, a: Tuple, b: Tuple) -> int:
    result = 0
    row1, row2 = min(a[0], b[0]), max(a[0], b[0])
    col1, col2 = min(a[1], b[1]), max(a[1], b[1])
    for i in range(row1 + 1, row2 + 1):
        result += 1000000 if i in emptyRows else 1
    for j in range(col1 + 1, col2 + 1):
        result += 1000000 if j in emptyCols else 1
    return result


def solve(document):
    data = [[c for c in row if c != '\n'] for row in document]
    galaxy = np.array(data)
    emptyRows = set([i for i, line in enumerate(galaxy) if all(line == '.')])
    emptyCols = set([i for i, line in enumerate(galaxy.T) if all(line == '.')])
    positions = findGalaxyPositions(galaxy)

    distances = []
    for i, positionA in enumerate(positions):
        for j, positionB in enumerate(positions):
            if i == j or i > j:
                continue
            distances.append((i, j, getGalaxyDistance(
                emptyRows, emptyCols, positionA, positionB)))

    # take shortest distance for each galaxy
    distances = sorted(distances, key=lambda x: x[2])
    result = 0
    added = set()
    for y, x, d in distances:
        if (y, x) in added:
            continue
        result += d
        added.add((y, x))
    
    print(result)


if __name__ == "__main__":
    with open(f"{os.getcwd()}/{DAY}/{input('Enter the input file id: ')}.input", "r") as document:
        solve(document)
