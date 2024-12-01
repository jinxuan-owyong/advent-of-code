# --- Day 2: Cube Conundrum ---
import os
from collections import defaultdict
DAY = "02"

R = "red"
G = "green"
B = "blue"


def readDraw(draw):
    count = defaultdict(lambda: 0)
    for balls in draw.split(","):
        numBalls, colour = balls.lstrip(" ").split(" ")
        count[colour.rstrip("\n")] = int(numBalls)
    return count


def readGame(game):
    game = game[5:]
    gameNum, game = game.split(":")
    return int(gameNum), [readDraw(d) for d in game.split(";")]


def solve(document):
    result = 0
    for line in document:
        _, gameData = readGame(line)
        redRequired = max(map(lambda draw: draw[R], gameData))
        greenRequired = max(map(lambda draw: draw[G], gameData))
        blueRequired = max(map(lambda draw: draw[B], gameData))
        result += redRequired * blueRequired * greenRequired
    print(result)


if __name__ == "__main__":
    with open(f"{os.getcwd()}/{DAY}/{input('Enter the input file id: ')}.input", "r") as document:
        solve(document)
        pass
