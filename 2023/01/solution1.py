# --- Day 1: Trebuchet?! ---
import os
DAY = '01'

# part 1


def findFirstNumber(s):
    for c in s:
        if f'{c}'.isnumeric():
            return c


def findLastNumber(s):
    for c in s[::-1]:
        if f'{c}'.isnumeric():
            return c


def solve(document):
    total = 0
    for line in document:
        total += int(findFirstNumber(line) + findLastNumber(line))
    print(total)


if __name__ == "__main__":
    with open(f"{os.getcwd()}/{DAY}/{input('Enter the input file id: ')}.input", "r") as document:
        solve(document)
