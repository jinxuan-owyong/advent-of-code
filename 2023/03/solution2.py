# --- Day 3: Gear Ratios ---
import os
from typing import List, Tuple
DAY = "03"

# part 2


def findAsteriskSymbols(schematic: List[str]) -> List[Tuple[int, int]]:
    symbols = []
    for i, row in enumerate(schematic):
        for j, col in enumerate(row):
            if col == '*':
                symbols.append((i, j))

    return symbols


def findWholeNumber(schematic: List[List[str]], i: int, j: int) -> int:
    left = j
    right = j
    while left > 0 and schematic[i][left - 1].isnumeric():
        left -= 1
    while right < len(schematic[0]) - 1 and schematic[i][right + 1].isnumeric():
        right += 1
    return int(schematic[i][left:right + 1])


def findAdjacentPartNumbers(schematic: List[List[str]], i: int, j: int) -> List[int]:
    neighbours = []
    hasN = i > 0
    hasS = i < len(schematic) - 1
    hasE = j < len(schematic[0]) - 1
    hasW = j > 0

    if hasN and schematic[i - 1][j].isnumeric():  # N
        neighbours.append((i - 1, j))
    if hasS and schematic[i + 1][j].isnumeric():  # S
        neighbours.append((i + 1, j))
    if hasE and schematic[i][j + 1].isnumeric():  # E
        neighbours.append((i, j + 1))
    if hasW and schematic[i][j - 1].isnumeric():  # W
        neighbours.append((i, j - 1))
    if hasN and hasW and schematic[i - 1][j - 1].isnumeric():  # NW
        neighbours.append((i - 1, j - 1))
    if hasN and hasE and schematic[i - 1][j + 1].isnumeric():  # NE
        neighbours.append((i - 1, j + 1))
    if hasS and hasW and schematic[i + 1][j - 1].isnumeric():  # SW
        neighbours.append((i + 1, j - 1))
    if hasS and hasE and schematic[i + 1][j + 1].isnumeric():  # SE
        neighbours.append((i + 1, j + 1))

    # remove duplicates for long numbers
    return list(set(map(lambda n: findWholeNumber(schematic, *n), neighbours)))


def solve(document):
    schematic = [line.rstrip('\n') for line in document]
    asterisks = findAsteriskSymbols(schematic)
    # A gear is any * symbol that is adjacent to exactly two part numbers.
    asteriskParts = map(
        lambda a: findAdjacentPartNumbers(schematic, *a), asterisks)
    gears = filter(lambda x: len(x) == 2, asteriskParts)
    gearRatios = map(lambda x: x[0] * x[1], gears)
    print(sum(gearRatios))


if __name__ == "__main__":
    with open(f"{os.getcwd()}/{DAY}/{input('Enter the input file id: ')}.input", "r") as document:
        solve(document)