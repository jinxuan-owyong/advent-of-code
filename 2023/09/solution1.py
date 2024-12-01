# --- Day 9: Mirage Maintenance ---
import os
from typing import List
DAY = "09"

# part 1


def findNext(sequence: List[int]):
    diff = []
    for i in range(len(sequence) - 1):
        diff.append(sequence[i + 1] - sequence[i])
    if len(set(diff)) == 1:  # constant difference
        return diff[0]
    else: # recursively calculate difference of next level
        return diff[-1] + findNext(diff)


def solve(document):
    history = [list(map(int, line.split(' '))) for line in document]
    result = 0
    for h in history:
        result += h[-1] + findNext(h)
    print(result)


if __name__ == "__main__":
    with open(f"{os.getcwd()}/{DAY}/{input('Enter the input file id: ')}.input", "r") as document:
        solve(document)
