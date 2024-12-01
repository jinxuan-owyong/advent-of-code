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
        gameNum, gameData = readGame(line)
        impossibleDraws = list(
            filter(lambda draw: draw[R] > 12 or draw[G] > 13 or draw[B] > 14, gameData))
        if len(impossibleDraws) == 0:
            result += gameNum
    print(result)


if __name__ == "__main__":
    with open(f"{os.getcwd()}/{DAY}/{input('Enter the input file id: ')}.input", "r") as document:
        solve(document)
        pass
