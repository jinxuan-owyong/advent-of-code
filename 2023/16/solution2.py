# --- Day 16: The Floor Will Be Lava ---
import os
from typing import List, Tuple
DAY = "16"

# part 2


reflectBeam = {
    '/': {'N': 'E', 'E': 'N', 'S': 'W', 'W': 'S'},
    '\\': {'N': 'W', 'W': 'N', 'S': 'E', 'E': 'S'}
}


def reflectAndMoveBeam(mirror: str, beam: Tuple):
    y, x, direction = beam
    newDirection = reflectBeam[mirror][direction]
    return move((y, x, newDirection))


def move(beam: Tuple):
    y, x, direction = beam
    match direction:
        case 'N':
            return (y - 1, x, direction)
        case 'S':
            return (y + 1, x, direction)
        case 'E':
            return (y, x + 1, direction)
        case 'W':
            return (y, x - 1, direction)
        case _:
            assert False


# DFS to energize cells
def solve(grid: List[str], beam: Tuple):
    energized = set()
    visited = set()
    stack = [beam]

    while stack:
        curr = stack.pop()
        y, x, direction = curr
        if curr in visited \
                or x < 0 or x == len(grid[0]) or y < 0 or y == len(grid):
            continue

        visited.add(curr)
        energized.add((y, x))

        cell = grid[y][x]
        if cell == '.' \
                or cell == '|' and direction in ('N', 'S') \
                or cell == '-' and direction in ('W', 'E'):
            stack.append(move(curr))
        elif cell == '|' and direction in ('W', 'E'):
            stack.append((y, x, 'N'))
            stack.append((y, x, 'S'))
        elif cell == '-' and direction in ('N', 'S'):
            stack.append((y, x, 'W'))
            stack.append((y, x, 'E'))
        elif cell == '/' or '\\':
            stack.append(reflectAndMoveBeam(cell, curr))

    return len(energized)


if __name__ == "__main__":
    with open(f"{os.getcwd()}/{DAY}/{input('Enter the input file id: ')}.input", "r") as document:
        maxResult = (0, 0, 0)
        grid = [[c for c in row if c != '\n'] for row in document]
        for i, direction in ((0, 'S'), (len(grid) - 1, 'N')):
            for j in range(len(grid[0])):
                result = -1
                result = solve(grid, (i, j, direction))    
                if result > maxResult[0]:
                    maxResult = (result, i, j)
        for j, direction in ((0, 'E'), (len(grid[0]) - 1, 'W')):
            for i in range(len(grid)):
                result = -1
                result = solve(grid, (i, j, direction))    
                if result > maxResult[0]:
                    maxResult = (result, i, j)

        print(maxResult)
