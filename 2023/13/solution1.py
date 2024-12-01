# --- Day 13: Point of Incidence ---
import os
from typing import List
import numpy as np
DAY = "13"

# part 1


# columns -> rows to reuse logic
def transpose(grid: List[str]):
    gridNP = np.array([[c for c in row] for row in grid])
    return [''.join(row) for row in gridNP.T]


# look for two rows that are the same
def findPossibleMirror(pattern: List[str]):
    for i, _ in enumerate(pattern):
        if i == len(pattern) - 1:
            break
        if (pattern[i] == pattern[i + 1]):
            yield i + 1


def isValidMirror(pattern: List[str], mirror: int):
    i = mirror - 1
    j = mirror
    while i >= 0 and j < len(pattern):
        if pattern[i] != pattern[j]:
            return False
        i -= 1
        j += 1
    return True


# returns the index to the right/bottom of the mirror
def solve(pattern: List[str]):
    for i in findPossibleMirror(pattern):
        if isValidMirror(pattern, i):
            return i
    return -1


if __name__ == "__main__":
    with open(f"{os.getcwd()}/{DAY}/{input('Enter the input file id: ')}.input", "r") as document:
        patterns = document.read().split('\n\n')
        result = 0
        for p in patterns:
            p = p.split('\n')
            rowIdx = solve(p)
            colIdx = solve(transpose(p))
            if rowIdx > 0:
                result += rowIdx * 100
            elif colIdx > 0:
                result += colIdx
        print(result)
