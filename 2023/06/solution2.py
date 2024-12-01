# --- Day 6: Wait For It ---
import os
from typing import Tuple
DAY = "06"

# part 2


def processInupt(document) -> Tuple[int, int]:
    rawData = map(lambda x: x.rstrip('\n'), list(document))
    timeData, distData = map(lambda x: x.split(':'), rawData)
    timeData = ''.join(filter(lambda x: x != '', timeData[1].split(' ')))
    distData = ''.join(filter(lambda x: x != '', distData[1].split(' ')))
    return int(timeData), int(distData)


def findMinSpeed(time, dist) -> int:
    for speed in range(0, time // 2):
        if speed * (time - speed) > dist:
            return speed
    return -1


def solve(document):
    time, dist = processInupt(document)
    minSpeed = findMinSpeed(time, dist)
    # 2 * minSpeed since distance travelled is symmetric about t // 2
    numPossibilities = (time + 1) - (2 * minSpeed)
    print(numPossibilities)


if __name__ == "__main__":
    with open(f"{os.getcwd()}/{DAY}/{input('Enter the input file id: ')}.input", "r") as document:
        solve(document)
