# --- Day 14: Parabolic Reflector Dish ---
import os
from typing import List
import numpy as np
import re
from collections import Counter
DAY = "14"

# part 2


# calculates load when left of the platform is north
def calcLoad(platform: List[str]):
    load = 0
    for row in platform:
        for i, c in enumerate(row):
            if c != 'O':
                continue
            load += len(row) - i
    return load


def tiltLeft(platform: List[str]):
    def numRocks(x): return x[1] - x[0]
    tilted = []
    for row in platform:
        rocks = [rock.span() for rock in re.finditer('#+', ''.join(row))]
        result = []
        if not rocks:
            count = Counter(row)
            result.extend(['O'] * count['O'])
            result.extend(['.'] * count['.'])
            tilted.append(result)
            continue

        prev = [0, 0]
        for rock in rocks:
            count = Counter(row[prev[1]:rock[0]])
            result.extend(['O'] * count['O'])
            result.extend(['.'] * count['.'])
            result.extend(['#'] * numRocks(rock))
            prev = rock

        if rocks[-1][1] != len(row):
            count = Counter(row[prev[1]:])
            result.extend(['O'] * count['O'])
            result.extend(['.'] * count['.'])

        tilted.append(result)
    return tilted


# used for hashing/displaying the platform
def stringify(platform: np.ndarray):
    return [''.join(row) for row in platform]


def executeTiltCycle(platform: np.ndarray):
    # rotate tilt direction to face the left side
    platform = tiltLeft(np.rot90(platform, 1)) # north
    platform = tiltLeft(np.rot90(platform, -1)) # west
    platform = tiltLeft(np.rot90(platform, -1)) # south
    platform = tiltLeft(np.rot90(platform, -1)) # east
    return np.rot90(platform, 2)


# assumption: pattern repeats exists in tilt cycle
def findCycleSize(platform: np.ndarray):
    seen = set()
    position = {}
    count = 0
    while True:
        platform = executeTiltCycle(platform)
        hashed = tuple(map(hash, stringify(platform)))
        if hashed in seen: # found cycle
            break
        seen.add(hashed)
        position[hashed] = count
        count += 1
    return (count - position[hashed]), position[hashed], platform
    

def solve(platform: List[str]):
    cycleCount, offset, cycleStart = findCycleSize(platform)
    for _ in range(((1000000000 - offset) % cycleCount - 1)):
        cycleStart = executeTiltCycle(cycleStart)
    return calcLoad(np.rot90(cycleStart, 1))


if __name__ == "__main__":
    with open(f"{os.getcwd()}/{DAY}/{input('Enter the input file id: ')}.input", "r") as document:
        result = solve(np.array([[c for c in row if c != '\n'] for row in document]))
        print(result)
