# --- Day 7: Camel Cards ---
import os
from collections import defaultdict
DAY = "07"

# part 2


class Hand:
    def __init__(self, rawData) -> None:
        self.cards = defaultdict(lambda: 0)
        cards, bid = rawData.split(' ')
        countJ = 0

        for c in cards:
            if c == 'J':
                countJ += 1
                continue
            self.cards[c] += 1

        cardsFrequency = sorted(self.cards.items(), key=lambda x: (
            x[1], self.getCardStrength(x[0])), reverse=True)
        if countJ == 5:
            # strongest hand
            self.cards['A'] = 5
        else:
            # add J to the best/most frequent card
            self.cards[cardsFrequency[0][0]] += countJ

        self.bid = int(bid)
        # original cards string since Js are the weakest
        self.cardsList = [c for c in cards]
        self.totalCardStrength = self.getTotalCardStrength()

    @staticmethod
    def getCardStrength(card: str) -> int:
        strengths = {'A': 14, 'K': 13, 'Q': 12, 'T': 10, 'J': 1}
        return int(card) if card.isnumeric() else strengths[card]

    def getTotalCardStrength(self) -> int:
        # max card strength = 14 (4 bits)
        # total 5 cards, total strength should only be used as tie-breaker
        result = 0
        for c in self.cardsList:
            result = result << 4
            result |= self.getCardStrength(c)
        return result

    def getHandStrength(self) -> int:
        if self.isNOfAKind(5):
            return 6
        if self.isNOfAKind(4):
            return 5
        if self.isFullHouse():
            return 4
        if self.isNOfAKind(3):
            return 3
        if self.isNPairs(2):
            return 2
        if self.isNPairs(1):
            return 1
        if self.isHighCard():
            return 0
        raise Exception('unexpected hand')

    def isNOfAKind(self, n) -> bool:
        return len(list(filter(lambda x: x[1] == n, self.cards.items()))) == 1

    def isFullHouse(self) -> bool:
        return self.isNOfAKind(3) and self.isNOfAKind(2)

    def isNPairs(self, n: int) -> bool:
        return len(list(filter(lambda x: x[1] == 2, self.cards.items()))) == n

    def isHighCard(self) -> bool:
        return len(list(set(self.cardsList)))


def solve(document):
    hands = [Hand(line) for line in document]
    winningOrder = sorted(hands, key=lambda h: (
        h.getHandStrength(), h.getTotalCardStrength()))
    result = 0
    for idx, hand in enumerate(winningOrder):
        result += (idx + 1) * hand.bid
    print(result)


if __name__ == "__main__":
    with open(f"{os.getcwd()}/{DAY}/{input('Enter the input file id: ')}.input", "r") as document:
        solve(document)
