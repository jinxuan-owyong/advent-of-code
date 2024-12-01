# --- Day 10: Pipe Maze ---
import os
from typing import List, Tuple
import queue
DAY = "10"

# part 1


def findStart(grid: List[str]) -> Tuple[int, int]:
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == 'S':
                return (i, j)
    assert False


# BFS, returns number of steps taken to traverse loop
def explore(grid: List[str], start: Tuple[int, int]) -> int:
    q = queue.Queue()
    q.put(start)
    count = 0
    first = True
    visited = set()
    connectors = {
        'left': ('L', 'F', '-', 'S'),
        'right': ('7', 'J', '-', 'S'),
        'up': ('F', '7', '|', 'S'),
        'down': ('L', 'J', '|', 'S')
    }

    while not q.empty():
        y, x = q.get()
        if (y, x) in visited:
            continue
        visited.add((y, x))
        
        hasLeft = (x > 0) \
            and (grid[y][x] in connectors['right']) \
            and (grid[y][x - 1] in connectors['left'])
        hasRight = (x < len(grid[0]) - 1) \
            and (grid[y][x] in connectors['left']) \
            and (grid[y][x + 1] in connectors['right'])
        hasUp = (y > 0) \
            and (grid[y][x] in connectors['down']) \
            and (grid[y - 1][x] in connectors['up'])
        hasDown = (y < len(grid[0]) - 1) \
            and (grid[y][x] in connectors['up']) \
            and (grid[y + 1][x] in connectors['down'])

        # returned back to start
        if (y, x) == start and not first:
            return count

        if hasLeft:
            q.put((y, x - 1))
        if hasRight:
            q.put((y, x + 1))
        if hasUp:
            q.put((y - 1, x))
        if hasDown:
            q.put((y + 1, x))

        count += 1
        first = False

    return count


def solve(document):
    grid = [line.rstrip('\n') for line in document]
    start = findStart(grid)
    steps = explore(grid, start)
    print(steps // 2)


if __name__ == "__main__":
    with open(f"{os.getcwd()}/{DAY}/{input('Enter the input file id: ')}.input", "r") as document:
        solve(document)
