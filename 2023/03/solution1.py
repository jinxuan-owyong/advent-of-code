# --- Day 3: Gear Ratios ---
import os
import re
from typing import List, Tuple
DAY = "03"

# part 1


def isSymbol(c):
    return not f'{c}'.isnumeric() and c != '.'


def hasAdjacentSymbol(schematic: List[List[str]], i: int, j: int, num: str) -> List[int]:
    for _ in num:
        hasN = i > 0
        hasS = i < len(schematic) - 1
        hasE = j < len(schematic[0]) - 1
        hasW = j > 0

        if (hasN and isSymbol(schematic[i - 1][j])) \
                or (hasS and isSymbol(schematic[i + 1][j])) \
                or (hasE and isSymbol(schematic[i][j + 1])) \
                or (hasW and isSymbol(schematic[i][j - 1])) \
                or (hasN and hasW and isSymbol(schematic[i - 1][j - 1])) \
                or (hasN and hasE and isSymbol(schematic[i - 1][j + 1])) \
                or (hasS and hasW and isSymbol(schematic[i + 1][j - 1])) \
                or (hasS and hasE and isSymbol(schematic[i + 1][j + 1])):
            return True

        j += 1

    return False


def findPartNumbers(schematic: List[str]) -> List[int]:
    partNumbers = []
    matches = list(map(lambda row: re.finditer("[0-9]+", row), schematic))

    for i, row in enumerate(matches):
        for num in row:
            if (hasAdjacentSymbol(schematic, i, num.start(), num.group())):
                partNumbers.append(int(num.group()))

    return partNumbers


def solve(document):
    schematic = [line.rstrip('\n') for line in document]
    partNumbers = findPartNumbers(schematic)
    print(sum(partNumbers))


if __name__ == "__main__":
    with open(f"{os.getcwd()}/{DAY}/{input('Enter the input file id: ')}.input", "r") as document:
        solve(document)
        pass
