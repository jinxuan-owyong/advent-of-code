# --- Day 17: Clumsy Crucible ---
import os
from typing import List
from enum import Enum
from heapq import heappop, heappush
import sys
DAY = "17"

# part 1


class Direction(Enum):
    NORTH = (-1, 0)
    SOUTH = (1, 0)
    EAST = (0, 1)
    WEST = (0, -1)

    def __lt__(self, other):
        True


turnLeft = {
    Direction.NORTH: Direction.WEST,
    Direction.SOUTH: Direction.EAST,
    Direction.EAST: Direction.NORTH,
    Direction.WEST: Direction.SOUTH
}

turnRight = {
    Direction.NORTH: Direction.EAST,
    Direction.SOUTH: Direction.WEST,
    Direction.EAST: Direction.SOUTH,
    Direction.WEST: Direction.NORTH
}

reverse = {
    Direction.NORTH: Direction.SOUTH,
    Direction.SOUTH: Direction.NORTH,
    Direction.EAST: Direction.WEST,
    Direction.WEST: Direction.EAST
}


def solve(grid: List[str]):
    # # (not) dijkstra's algorithm
    # dist = [[-1 for _ in row] for row in grid] # each (i, j) is a vertex
    # dist[0][0] = 0
    # (priority, (y, x, currDir, dirCount))
    frontier = [(0, (0, 0, Direction.EAST, 0))]
    explored = set()
    while frontier:
        pathWeight, (y, x, currDir, dirCount) = heappop(frontier)
        # in normal dijkstra, this check tells us that we have already found the shortest path to the node
        # but in this modification, we want to check if the combination of (y, x, currDir, dirCount) is seen?
        # if pathWeight > dist[y][x] and : # "outdated" frontier
        #     continue
        if (y, x, currDir, dirCount) in explored:
            continue
        explored.add((y, x, currDir, dirCount))
        if y == len(grid) - 1 and x == len(grid[0]) - 1:
            return pathWeight
        for d in Direction:
            if d == reverse[currDir] or (dirCount < 4 and d != currDir) or (dirCount == 10 and d == currDir):
                continue
            deltaY, deltaX = d.value
            nextY, nextX = y + deltaY, x + deltaX
            # invalid next step
            if nextY < 0 or nextY == len(grid) or nextX < 0 or nextX == len(grid[0]):
                continue

            stepWeight = pathWeight + grid[nextY][nextX]

            # irrelevant in this case since we do not require the relax step
            # if dist[nextY][nextX] == -1 or stepWeight < dist[nextY][nextX]: # "relax"
            #     dist[nextY][nextX] = stepWeight

            # we search all possible paths unlike in dijkstra
            if d == currDir:
                heappush(frontier, (stepWeight, (nextY, nextX, d, dirCount + 1)))
            else:
                # 1 since already taken a step
                heappush(frontier, (stepWeight, (nextY, nextX, d, 1)))

    # for row in dist:
    #     print(row)
    # print(dist[-1][-1])


if __name__ == "__main__":
    with open(f"{os.getcwd()}/{DAY}/{input('Enter the input file id: ')}.input", "r") as document:
        result = solve([list(map(int, row.rstrip('\n'))) for row in document])
        print(result)
