# --- Day 5: If You Give A Seed A Fertilizer ---
import os
from typing import Dict, List, Tuple
import re
import bisect
import queue
DAY = "05"

# part 2


def processInput(data: List[str]) -> Tuple[List[int], List[List[List[int]]]]:
    def matchTitle(line): return line[0], re.match('\w+-\w+-\w+ map:', line[1])
    def isValidMatch(x): return x[1] != None

    def getMapData(idx):
        # extract lines containing map data by index
        return data[idx[0]:idx[1] + 1]

    def createBAMap(mappings):
        # split each mapping into dest, src, and size, then convert to int
        BAMap = map(lambda x: list(
            map(int, x.split(' '))), mappings)
        return sorted(BAMap, key=lambda x: x[0])  # sort by ascending dest

    # extract seed numbers from first line
    seedNumbers = map(int, filter(lambda x: x != '',
                      data[0].split(':')[1].split(' ')))

    # find start row index in data array for each map title
    mapStart = sorted(filter(isValidMatch, map(
        matchTitle, enumerate(data))), key=lambda x: x[0])

    # find index range in data array for each map
    mapTitles = []
    for i, (start, _) in enumerate(mapStart):
        end = mapStart[i + 1][0] - \
            1 if (i != len(mapStart) - 1) else len(data) - 1
        mapTitles.append((start + 1, end))  # entries for each map

    ABMaps = list(map(createBAMap, map(getMapData, mapTitles)))
    ABMaps.reverse()
    return list(seedNumbers), ABMaps


# def findMappedDestination(BAMap: List[List[int]], a: int) -> int:
#     # check if a in source range
#     if a < BAMap[0][1] or (a > BAMap[-1][1] + BAMap[-1][2]):
#         return a
#     idx = bisect.bisect(BAMap, a, key=lambda x: x[1] + x[2])
#     dest, src, _ = BAMap[idx]
#     return a + (dest - src)

# requires map to be sorted in ascending order of target column
def findMappedSource(BAMap: List[List[int]], B: int) -> int:
    # from A to B, if A exceed B's range, then A remains unchanged
    # otherwise it is a 1-1 mapping
    # hence from B to A, the range of B will always be a subset of A
    # and we do not need to check if B's range exceed A
    # bisect_left returns the index of the containing range if B < dest + size
    idx = bisect.bisect_left(BAMap, B, key=lambda x: x[0] + x[2])
    mapCeil = BAMap[-1][0] + BAMap[-1][2] - 1
    if (idx == len(BAMap)):
        if B == mapCeil:  # B is the last element in range
            idx -= 1
        else:  # B not in map range
            return -1
    dest, src, _ = BAMap[idx]
    return B + (src - dest)


def findValidSeedRange(BAMaps: List[List[int]], location: Tuple[int, int, int]) -> Tuple[int, int]:
    # currQ = queue.Queue()
    # nextQ = queue.Queue()
    # currQ.put((location[0], location[2])) # initial location, initial size
    # for BAMap in BAMaps:
    #     while not currQ.empty():
    #         num, ASize = findMappedSource(BAMap, currQ.get())
    #         if BSize < ASize:
    #             nextQ.put()
    #             currQ.put(num + BSize)
    #         nextQ.put()
    #     currQ = nextQ
    #     nextQ = queue.Queue()
    # return list(currQ)
    num, _, size = location
    for BAMap in BAMaps:
        temp = findMappedSource(BAMap, num)
        num = temp if temp != -1 else num  # update num if num in map range
    return (num, size)


def filterValidSeeds(seeds: List[int], validRanges: List[Tuple[int, int]]):
    result = []
    
    for i in range(0, len(seeds), 2):
        seedStart, seedSize = seeds[i], seeds[i + 1]
        seedEnd = seedStart + seedSize - 1
        idx = bisect.bisect_left(validRanges, seedStart, key=lambda x: x[0] + x[1])
        if idx == len(validRanges):
            continue
        validStart, validSize = validRanges[idx]
        validEnd = validStart + validSize - 1
        seedDistance = seedStart - validStart
        # if seedEnd <= validEnd:
        #     result.append((seedStart, seedSize))
        #     continue
        # validStart <= seedStart always
        
        if validStart <= seedStart:
            if validEnd > seedEnd:
                result.append((seedStart, seedSize))
            else:
                result.append((seedStart, validSize - seedDistance))
        else:
            if validEnd <= seedEnd:
                result.append((validStart, validSize))
            else:
                seedDistance = validStart - seedStart
                result.append((validStart, seedSize - seedDistance))
        
        
        
        
        
        
        
        
        
        
        
        
        # if validStart == seedStart:
        #     # valid: |            |
        #     # seed : |       |    |        |
        #     if seedSize <= validSize:
        #         result.append((seedStart, seedSize))
        #     else:
        #         result.append((seedStart, validSize))
        # elif validStart < seedStart:
        #     # valid: |               |
        #     # seed :    |       |    |        | 
        #     seedDistance = seedStart - validStart
        #     if seedSize <= (validSize - seedDistance):
        #         result.append((seedStart, seedSize))
        #     else:
        #         result.append((seedStart, validSize - seedDistance))
        # else:
        #     raise Exception("Error")
                    
    return result
            


def solve(document):
    data = [line.rstrip('\n')
            for line in filter(lambda x: x != '\n', document)]
    seeds, BAMaps = processInput(data)
    # reverse lookup based on possible locations 
    validSeedRanges = sorted([findValidSeedRange(
        BAMaps, location) for location in BAMaps[0]], key=lambda x: x[0])
    for s in (sorted(filterValidSeeds(seeds, validSeedRanges), key=lambda x: x[0])):
        print(s)


if __name__ == "__main__":
    with open(f"{os.getcwd()}/{DAY}/{input('Enter the input file id: ')}.input", "r") as document:
        solve(document)
