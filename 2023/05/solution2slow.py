# --- Day 5: If You Give A Seed A Fertilizer ---
import os
from typing import Dict, List, Tuple
import re
import bisect
DAY = "05"

# part 2


def processInput(data: List[str]) -> Tuple[List[int], List[List[List[int]]]]:
    def matchTitle(line): return line[0], re.match('\w+-\w+-\w+ map:', line[1])
    def isValidMatch(x): return x[1] != None

    def getMapData(idx):
        # extract lines containing map data by index
        return data[idx[0]:idx[1] + 1]

    def createABMap(mappings):
        # split each mapping into dest, src, and size, then convert to int
        ABMap = map(lambda x: list(
            map(int, x.split(' '))), mappings)
        return sorted(ABMap, key=lambda x: x[1])  # sort by ascending src

    # extract seed numbers from first line
    seedNumbers = map(int, filter(lambda x: x != '',
                      data[0].split(':')[1].split(' ')))

    # find start index for each map title
    mapStart = sorted(filter(isValidMatch, map(
        matchTitle, enumerate(data))), key=lambda x: x[0])

    # find index range for each map
    mapTitles = []
    for i, (start, _) in enumerate(mapStart):
        end = mapStart[i + 1][0] - \
            1 if (i != len(mapStart) - 1) else len(data) - 1
        mapTitles.append((start + 1, end))  # entries for each map

    return list(seedNumbers), list(map(createABMap, map(getMapData, mapTitles)))


def findMappedDestination(ABMap: List[List[int]], a: int) -> int:
    # check if a in source range
    if a < ABMap[0][1] or (a >= ABMap[-1][1] + ABMap[-1][2]):
        return a
    idx = bisect.bisect(ABMap, a, key=lambda x: x[1] + x[2])
    dest, src, _ = ABMap[idx]
    return a + (dest - src)

def findLocation(ABMaps, seed):
    num = seed
    for ABMap in ABMaps:
        num = findMappedDestination(ABMap, num)
    return num

def solve(document):
    data = [line.rstrip('\n')
            for line in filter(lambda x: x != '\n', document)]
    seeds, ABMaps = processInput(data)
    minLocation = 1E10
    for i in range(0, len(seeds), 2):
        seedStart, seedCount = seeds[i], seeds[i + 1]
        for seed in range(seedStart, seedStart + seedCount):
            print((seed, findLocation(ABMaps, seed)))
            minLocation  = min(findLocation(ABMaps, seed), minLocation)
            
    print(minLocation)

if __name__ == "__main__":
    with open(f"{os.getcwd()}/{DAY}/{input('Enter the input file id: ')}.input", "r") as document:
        solve(document)
