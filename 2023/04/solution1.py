# --- Day 4: Scratchcards ---
import os
from typing import List, Tuple
DAY = "04"

# part 1


def processCard(s: str) -> Tuple[int, List[int], List[int]]:
    def isNonEmptyString(x): return x != ''
    cardId, cardData = s.split(':')
    _, cardNum = filter(isNonEmptyString, cardId.split(' '))
    winningNums, scratchNums = cardData.rstrip('\n').split('|')
    winningNums = filter(isNonEmptyString, winningNums.split(' '))
    scratchNums = filter(isNonEmptyString, scratchNums.split(' '))
    return cardNum, list(winningNums), list(scratchNums)


def solve(document):
    cards = map(lambda line: processCard(line), document)
    matches = map(lambda card: len(set(card[1]).intersection(set(card[2]))), cards)
    points = map(lambda x: 2**(x - 1) if x > 0 else 0, matches)
    print(sum(points))


if __name__ == "__main__":
    with open(f"{os.getcwd()}/{DAY}/{input('Enter the input file id: ')}.input", "r") as document:
        solve(document)