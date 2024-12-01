# --- Day 10: Pipe Maze ---
import os
from typing import List, Tuple
import queue
DAY = "10"

# part 2

# indicate direction the cell
connectors = {
    'left': ('L', 'F', '-', 'S'),
    'right': ('7', 'J', '-', 'S'),
    'up': ('F', '7', '|', 'S'),
    'down': ('L', 'J', '|', 'S')
}


# given the current cell and the direction travelling in
# returns the turned direction
turnDirection = {
    'F': {'N': 'E', 'W': 'S'},
    'J': {'E': 'N', 'S': 'W'},
    '7': {'N': 'W', 'E': 'S'},
    'L': {'W': 'N', 'S': 'E'}
}


labelA = set()
labelB = set()


def findStart(grid: List[str]) -> Tuple:
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == 'S':
                return (i, j)
    assert False


# BFS, returns filtered grid only with loop
def exploreGrid(grid: List[str], start: Tuple) -> int:
    q = queue.Queue()
    q.put(start)
    count = 0
    first = True
    visited = set()
    loop = [['.' for x in row] for row in grid]

    while not q.empty():
        y, x = q.get()
        loop[y][x] = grid[y][x]

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

    return loop


# given the current cell and the previous cell,
# returns the next direction to travel in, and the next cell itself
def nextPipe(grid: List[List[str]], curr: Tuple, prev: Tuple) -> Tuple[str, Tuple]:
    currY, currX = curr
    prevY, prevX = prev
    match grid[currY][currX]:
        case '|':
            if currY > prevY:
                return 'S', (currY + 1, currX)
            else:
                return 'N', (currY - 1, currX)
        case '-':
            if currX > prevX:
                return 'E', (currY, currX + 1)
            else:
                return 'W', (currY, currX - 1)
        case 'L':
            if currY > prevY:
                return 'E', (currY, currX + 1)
            else:
                return 'N', (currY - 1, currX)
        case 'J':
            if currY > prevY:
                return 'W', (currY, currX - 1)
            else:
                return 'N', (currY - 1, currX)
        case '7':
            if currY == prevY:
                return 'S', (currY + 1, currX)
            else:
                return 'W', (currY, currX - 1)
        case 'F':
            if currY == prevY:
                return 'S', (currY + 1, currX)
            else:
                return 'E', (currY, currX + 1)
        case _:
            assert False


# returns one of the directions to traverse in from the starting position
def getInitialDirection(grid: List[List[str]], start: Tuple):
    y, x = start
    if x > 0 and grid[y][x - 1] in connectors['left']:
        direction = 'W'
        x -= 1
    elif x < len(grid[0]) - 1 and grid[y][x + 1] in connectors['right']:
        direction = 'E'
        x += 1
    elif y > 0 and grid[y - 1][x] in connectors['up']:
        direction = 'N'
        y -= 1
    elif x < len(grid[0]) - 1 and grid[y][x + 1] in connectors['down']:
        direction = 'S'
        y += 1
    return direction, (y, x)


# tracing along the loop will result in one side being
# always inside and the other being always outside
# given grid is updated with As and Bs located along loop
def traceLoop(grid: List[List[str]], start: Tuple):
    def isEmptyCell(x): return x == '.'

    def labelCell(pos, label):
        y, x = pos
        grid[y][x] = label
        match label:
            case 'A': labelA.add((y, x))
            case 'B': labelB.add((y, x))

    prev = start
    direction, curr = getInitialDirection(grid, start)
    turned = False

    while curr != start:
        y, x = curr

        # label sides A and B of the loop
        match direction:
            case 'N':
                if x > 0 and isEmptyCell(grid[y][x - 1]):
                    labelCell((y, x - 1), 'A')
                if x < len(grid[0]) - 1 and isEmptyCell(grid[y][x + 1]):
                    labelCell((y, x + 1), 'B')
            case 'S':
                if x > 0 and isEmptyCell(grid[y][x - 1]):
                    labelCell((y, x - 1), 'B')
                if x < len(grid[0]) - 1 and isEmptyCell(grid[y][x + 1]):
                    labelCell((y, x + 1), 'A')
            case 'W':
                if y > 0 and isEmptyCell(grid[y - 1][x]):
                    labelCell((y - 1, x), 'B')
                if y < len(grid) - 1 and isEmptyCell(grid[y + 1][x]):
                    labelCell((y + 1, x), 'A')
            case 'E':
                if y > 0 and isEmptyCell(grid[y - 1][x]):
                    labelCell((y - 1, x), 'A')
                if y < len(grid) - 1 and isEmptyCell(grid[y + 1][x]):
                    labelCell((y + 1, x), 'B')
            case _:
                assert False

        # repeat labelling if current cell is a corner
        if not turned and grid[y][x] in ('F', 'J', '7', 'L'):
            direction = turnDirection[grid[y][x]][direction]
            turned = True
            continue

        # reset turns for next cell
        turned = False
        temp = curr
        direction, curr = nextPipe(grid, curr, prev)
        prev = temp


# flood fill given positions of a label, returns number of cells of all islands
# updates grid with flood filled islands
def exploreLabel(grid: List[List[str]], positions: set, myLabel: str) -> int:
    q = queue.Queue()
    [q.put(p) for p in positions]
    visited = set()
    count = 0

    while not q.empty():
        curr = q.get()

        if curr in visited:
            continue
        visited.add(curr)

        directions = [(0, 0), (-1, 0), (0, -1), (1, 0), (0, 1)]
        for d in directions:
            y, x = curr[0] + d[0], curr[1] + d[1]
            if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]):
                continue

            if grid[y][x] == '.':
                q.put((y, x))
                grid[y][x] = myLabel

        count += 1

    return count


def solve(document):
    grid = [line.rstrip('\n') for line in document]
    start = findStart(grid)
    loop = exploreGrid(grid, start)
    traceLoop(loop, start)

    countA = exploreLabel(loop, labelA, 'A')
    countB = exploreLabel(loop, labelB, 'B')

    for r in loop:
        print(''.join(r))
    print('A:', countA)
    print('B:', countB)


if __name__ == "__main__":
    with open(f"{os.getcwd()}/{DAY}/{input('Enter the input file id: ')}.input", "r") as document:
        solve(document)
