# --- Day 11: Cosmic Expansion ---
import os
from typing import List, Tuple
import numpy as np
DAY = "11"

# part 1


# insert extra rows and columns if empty
def expandGalaxy(galaxy: np.ndarray) -> np.ndarray:
    emptyRows = [i for i, line in enumerate(galaxy) if all(line == '.')]
    emptyCols = [i for i, line in enumerate(galaxy.T) if all(line == '.')]
    # expand from last to first index to preserve row/col index order
    # length of row = num of cols
    _, m = galaxy.shape
    for row in emptyRows[::-1]:
        galaxy = np.insert(galaxy, row, ['.'] * m, axis=0)
    # height of col = num of rows
    n, _ = galaxy.shape
    for col in emptyCols[::-1]:
        galaxy = np.insert(galaxy, col, ['.'] * n, axis=1)
    return galaxy


# returns all positions matching #
def findGalaxyPositions(galaxy: np.ndarray) -> List[Tuple]:
    result = []
    for i, row in enumerate(galaxy):
        for j, cell in enumerate(row):
            if cell == '#':
                result.append((i, j))
    return result


def getGalaxyDistance(a: Tuple, b: Tuple) -> int:
    height = max(a[0], b[0]) - min(a[0], b[0])
    width = max(a[1], b[1]) - min(a[1], b[1])
    return height + width


def solve(document):
    data = [[c for c in row if c != '\n'] for row in document]
    galaxy = np.array(data)
    expanded = expandGalaxy(galaxy)
    positions = findGalaxyPositions(expanded)
    distances = np.zeros((len(positions), len(positions)))
    # calculate all possible distances between galaxies
    for i, positionA in enumerate(positions):
        for j, positionB in enumerate(positions):
            if i == j or i > j:
                continue
            distances[i][j] = getGalaxyDistance(positionA, positionB)
    print(int(sum(sum(distances))))


if __name__ == "__main__":
    with open(f"{os.getcwd()}/{DAY}/{input('Enter the input file id: ')}.input", "r") as document:
        solve(document)
