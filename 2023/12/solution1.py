# --- Day 12: Hot Springs ---
import os
from typing import List, Tuple
DAY = "12"

# part 1


def solve(springs: str, criteria: List[int]):
    stack = []
    while stack
    pass


if __name__ == "__main__":
    with open(f"{os.getcwd()}/{DAY}/{input('Enter the input file id: ')}.input", "r") as document:
        for line in document:
            springs, criteria = line.split(' ')
            springs = springs.rstrip('\n')
            criteria = list(map(int, criteria.split(',')))
            solve(springs, criteria)