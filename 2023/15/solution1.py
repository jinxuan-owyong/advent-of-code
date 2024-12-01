# --- Day 15: Lens Library ---
import os
DAY = "15"

# part 1


def solve(s: str):
    result = 0
    for c in s:
        result += ord(c)
        result *= 17
        result = result % 256
    return result
        
        
if __name__ == "__main__":
    with open(f"{os.getcwd()}/{DAY}/{input('Enter the input file id: ')}.input", "r") as document:
        strings = document.read().rstrip('\n').split(',')
        print(sum(map(solve, strings)))