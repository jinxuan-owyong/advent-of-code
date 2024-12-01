# --- Day 4: Scratchcards ---
import os
from typing import List, Tuple
from collections import defaultdict
DAY = "04"

# part 2


def processCard(s: str) -> Tuple[int, List[int], List[int]]:
    def isNonEmptyString(x): return x != ''
    cardId, cardData = s.split(':')
    _, cardNum = filter(isNonEmptyString, cardId.split(' '))
    winningNums, scratchNums = cardData.rstrip('\n').split('|')
    winningNums = filter(isNonEmptyString, winningNums.split(' '))
    scratchNums = filter(isNonEmptyString, scratchNums.split(' '))
    return int(cardNum), list(winningNums), list(scratchNums)


def solve(document):
    numCards = defaultdict(lambda: 0)
    cards = list(map(lambda line: processCard(line), document))
    matches = list(map(lambda card: len(
        set(card[1]).intersection(set(card[2]))), cards))

    for (cardNum, _, _), numMatch in zip(cards, matches):
        numCards[cardNum] += 1  # initial card given
        for i in range(1, numMatch + 1):
            # number of cards[i] won so far
            numCards[cardNum + i] += numCards[cardNum]

    # count number of cards in total
    print(sum(map(lambda x: x[1], numCards.items())))


if __name__ == "__main__":
    with open(f"{os.getcwd()}/{DAY}/{input('Enter the input file id: ')}.input", "r") as document:
        solve(document)
