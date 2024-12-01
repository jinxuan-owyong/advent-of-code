# --- Day 1: Trebuchet?! ---
import os
DAY = '01'

# part 2


def findFirstNumber(s):
    firstNum = (-1, -1)
    for i, c in enumerate(s):
        if f'{c}'.isnumeric():
            firstNum = (i, c)
            break

    positions = [
        {"value": "1", "pos": s.index("one") if "one" in s else -1},
        {"value": "2", "pos": s.index("two") if "two" in s else -1},
        {"value": "3", "pos": s.index("three") if "three" in s else -1},
        {"value": "4", "pos": s.index("four") if "four" in s else -1},
        {"value": "5", "pos": s.index("five") if "five" in s else -1},
        {"value": "6", "pos": s.index("six") if "six" in s else -1},
        {"value": "7", "pos": s.index("seven") if "seven" in s else -1},
        {"value": "8", "pos": s.index("eight") if "eight" in s else -1},
        {"value": "9", "pos": s.index("nine") if "nine" in s else -1}
    ]
    valid_positions = list(filter(lambda entry: entry["pos"] != -1, positions))
    firstWord = min(valid_positions, key=lambda entry: entry["pos"]) if len(
        valid_positions) > 0 else {"pos": -1}
    if firstNum[0] == -1:
        return firstWord["value"]
    if firstWord["pos"] == -1:
        return firstNum[1]
    if firstNum[0] < firstWord["pos"]:
        return firstNum[1]
    return firstWord["value"]


def findLastNumber(s):
    s = s[::-1]
    firstNum = (-1, -1)
    for i, c in enumerate(s):
        if f'{c}'.isnumeric():
            firstNum = (i, c)
            break

    positions = [
        {"value": "1", "pos": s.index("eno") if "eno" in s else -1},
        {"value": "2", "pos": s.index("owt") if "owt" in s else -1},
        {"value": "3", "pos": s.index("eerht") if "eerht" in s else -1},
        {"value": "4", "pos": s.index("ruof") if "ruof" in s else -1},
        {"value": "5", "pos": s.index("evif") if "evif" in s else -1},
        {"value": "6", "pos": s.index("xis") if "xis" in s else -1},
        {"value": "7", "pos": s.index("neves") if "neves" in s else -1},
        {"value": "8", "pos": s.index("thgie") if "thgie" in s else -1},
        {"value": "9", "pos": s.index("enin") if "enin" in s else -1}
    ]
    valid_positions = list(filter(lambda entry: entry["pos"] != -1, positions))
    firstWord = min(valid_positions, key=lambda entry: entry["pos"]) if len(
        valid_positions) > 0 else {"pos": -1}
    if firstNum[0] == -1:
        return firstWord["value"]
    if firstWord["pos"] == -1:
        return firstNum[1]
    if firstNum[0] < firstWord["pos"]:
        return firstNum[1]
    return firstWord["value"]


def solve(document):
    total = 0
    for line in document:
        total += int(findFirstNumber(line) + findLastNumber(line))
    print(total)


if __name__ == "__main__":
    with open(f"{os.getcwd()}/{DAY}/{input('Enter the input file id: ')}.input", "r") as document:
        solve(document)
