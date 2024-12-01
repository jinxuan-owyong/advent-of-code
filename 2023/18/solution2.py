# --- Day 18: Lavaduct Lagoon ---
import os
from typing import List

DAY = "18"

# part 2


direction = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}

def decodeInstructions(digPlan: List[List[str]]):
    hexCodes = map(lambda x: x[2].lstrip('(#').rstrip(')'), digPlan)
    return [(direction[x[-1]], int(x[:5], 16)) for x in hexCodes]

def calculatePositions(digPlan: List[List[str]]):
    y, x = 0, 0
    positions = []
    for direction, dist in digPlan:
        match direction:
            case 'L':
                x -= dist
            case 'R':
                x += dist
            case 'U':
                y -= dist
            case 'D':
                y += dist
        positions.append((y, x))
    return positions


def solve(digPlan: List[List[str]]):
    instructions = decodeInstructions(digPlan)
    # shoelace algorithm
    positions = calculatePositions(instructions)
    firstY, firstX = positions[0]
    lastY, lastX = positions[-1]
    left = lastX * firstY
    right = firstX * lastY * -1
    for i in range(len(positions) - 1):
        currY, currX = positions[i]
        nextY, nextX = positions[i + 1]
        left += currX * nextY
        right += nextX * currY
    innerArea = abs(left - right) / 2
    boundaryLength = sum(map(lambda x: x[1], instructions))
    # use pick's theorem to find area of polygon
    # https://www.reddit.com/r/adventofcode/comments/18lg2we/2023_day_18_why_1_instead_of_1/
    return innerArea + (boundaryLength / 2) + 1


if __name__ == "__main__":
    with open(f"{os.getcwd()}/{DAY}/{input('Enter the input file id: ')}.input", "r") as document:
        def extractData(x):
            a, b, c = x.rstrip('\n').split(' ')
            return a, int(b), c
        result = solve([extractData(row) for row in document])
        print(int(result))
