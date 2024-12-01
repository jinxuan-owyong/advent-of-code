# --- Day 13: Point of Incidence ---
import os
from typing import List, Tuple
import solution1 as part1

DAY = "13"

# part 2


# new function to check for difference
# no change to majority of logic
def isAtMostOneBitDifferent(a: str, b: str):
    count = 0
    for x, y in zip(a, b):
        if x != y:
            count += 1
    return count <= 1


# look for two rows that are (almost) the same
def findPossibleMirror(pattern: List[str]):
    for i, _ in enumerate(pattern):
        if i == len(pattern) - 1:
            break
        if isAtMostOneBitDifferent(pattern[i], pattern[i + 1]):
            yield i + 1


def isValidMirror(pattern: List[str], mirror: int):
    i = mirror - 1
    j = mirror
    while i >= 0 and j < len(pattern):
        if not isAtMostOneBitDifferent(pattern[i], pattern[j]):
            return False
        i -= 1
        j += 1
    return True


def solve(pattern: List[str], ignore: Tuple, currDirection: str):
    ignoreDirection, ignoreIdx = ignore
    for i in findPossibleMirror(pattern):
        # check for a different reflection line
        if ignoreDirection == currDirection and i == ignoreIdx:
            continue
        if isValidMirror(pattern, i):
            return i
    return -1


if __name__ == "__main__":
    with open(f"{os.getcwd()}/{DAY}/{input('Enter the input file id: ')}.input", "r") as document:
        patterns = document.read().split('\n\n')
        result = 0
        for p in patterns:
            p = p.split('\n')

            oldRowIdx = part1.solve(p)
            oldColIdx = part1.solve(part1.transpose(p))
            oldMirror = ('row', oldRowIdx) if oldRowIdx != -1 else (('col', oldColIdx) if oldColIdx != -1 else -1)
            
            rowIdx = solve(p, oldMirror, 'row')
            colIdx = solve(part1.transpose(p), oldMirror, 'col')
            if rowIdx > 0:
                result += rowIdx * 100
            elif colIdx > 0:
                result += colIdx
        print(result)
