# --- Day 6: Wait For It ---
import os
from typing import List, Tuple
DAY = "06"

# part 1


def processInupt(document) -> Tuple[List[int], List[int]]:
    rawData = map(lambda x: x.rstrip('\n'), list(document))
    timeData, distData = map(lambda x: x.split(':'), rawData)
    timeData = map(int, filter(lambda x: x != '', timeData[1].split(' ')))
    distData = map(int, filter(lambda x: x != '', distData[1].split(' ')))
    return timeData, distData


def findMinSpeed(time, dist):
    for speed in range(0, time // 2):
        if speed * (time - speed) > dist:
            return speed
    return -1


def solve(document):
    numPossibilities = 1
    for time, dist in zip(*processInupt(document)):
        minSpeed = findMinSpeed(time, dist)
        # 2 * minSpeed since distance travelled is symmetric about t // 2
        numPossibilities *= (time + 1) - (2 * minSpeed)
    print(numPossibilities)


if __name__ == "__main__":
    with open(f"{os.getcwd()}/{DAY}/{input('Enter the input file id: ')}.input", "r") as document:
        solve(document)
