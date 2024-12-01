# --- Day 14: Parabolic Reflector Dish ---
import os
from typing import List, Tuple
import numpy as np
import re
from collections import Counter
DAY = "14"

# part 1


# columns -> rows to reuse logic
def transpose(grid: List[str]):
    gridNP = np.array([[c for c in row] for row in grid])
    return [''.join(row) for row in gridNP.T]


def calcLoad(platform: List[str]):
    load = 0
    for row in platform:
        for i, c in enumerate(row):
            if c != 'O': continue
            load += len(row) - i
    return load

def solve(platform: List[str]):
    def numRocks(x): return x[1] - x[0]
    platform = transpose(platform)
    tilted = []
    for row in platform:
        rocks = [rock.span() for rock in re.finditer('#+', row)]
        result = ''
        if not rocks:
            count = Counter(row)
            result += 'O' * count['O']
            result += '.' * count['.']
            tilted.append(result)
            continue

        prev = [0, 0]
        for rock in rocks:
            count = Counter(row[prev[1]:rock[0]])
            result += 'O' * count['O']
            result += '.' * count['.']
            result += '#' * numRocks(rock)
            prev = rock

        if rocks[-1][1] != len(row):
            count = Counter(row[prev[1]:])
            result += 'O' * count['O']
            result += '.' * count['.']

        tilted.append(result)

    return calcLoad(tilted)

if __name__ == "__main__":
    with open(f"{os.getcwd()}/{DAY}/{input('Enter the input file id: ')}.input", "r") as document:
        result = solve([row.rstrip('\n') for row in document])
        print(result)
