# --- Day 15: Lens Library ---
import os
from typing import List
from collections import defaultdict
import solution1 as part1
DAY = "15"

# part 2


class Lens:
    def __init__(self, label: str, focalLength: int):
        self.label = label
        self.focalLength = focalLength


class Box:
    def __init__(self):
        self.container: List[Lens] = []
        self.labels = set()

    def insert(self, lens: Lens):
        for i, curr in enumerate(self.container):
            if curr.label == lens.label:
                self.container[i].focalLength = lens.focalLength
                return
        # lens not present
        self.container.append(lens)
        self.labels.add(lens.label)

    def remove(self, label: str):
        if label not in self.labels:
            return
        for i, curr in enumerate(self.container):
            if curr.label == label:
                self.labels.remove(label)
                del (self.container[i])
                break


# assumption: all lenses have unique labels
lensBoxId = defaultdict(lambda: -1)
boxes = {}
for i in range(256):
    boxes[i] = Box()


def solve(s: str):
    if len(s.split('=')) > 1:
        label, focalLength = s.split('=')
        boxNum = part1.solve(label)
        boxes[boxNum].insert(Lens(label, int(focalLength)))
        lensBoxId[label] = boxNum
    elif len(s.split('-')) > 1:
        label, _ = s.split('-')
        boxNum = part1.solve(label)
        if label in lensBoxId:
            boxes[lensBoxId[label]].remove(label)
            del (lensBoxId[label])


if __name__ == "__main__":
    with open(f"{os.getcwd()}/{DAY}/{input('Enter the input file id: ')}.input", "r") as document:
        strings = document.read().rstrip('\n').split(',')
        for s in strings:
            solve(s)

        result = 0
        for boxNum, box in boxes.items():
            for i, lens in enumerate(box.container):
                result += (boxNum + 1) * (i + 1) * lens.focalLength
        print(result)
