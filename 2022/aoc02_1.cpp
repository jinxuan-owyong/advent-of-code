#include <iostream>
#include <unordered_map>

enum {
    ROCK = 1,
    PAPER = 2,
    SCISSORS = 3
};

enum {
    WIN = 6,
    DRAW = 3,
    LOSE = 0
};

std::unordered_map<char, int> MOVE = {
    {'A', ROCK},
    {'B', PAPER},
    {'C', SCISSORS},
    {'X', ROCK},
    {'Y', PAPER},
    {'Z', SCISSORS}};

int score_part_one(char x, char y) {
    int opp = MOVE[x];
    int own = MOVE[y];
    int sum = own;

    if (opp == ROCK && own == ROCK ||
        opp == PAPER && own == PAPER ||
        opp == SCISSORS && own == SCISSORS) {
        sum += DRAW;
    } else if (opp == ROCK && own == PAPER ||
               opp == PAPER && own == SCISSORS ||
               opp == SCISSORS && own == ROCK) {
        sum += WIN;
    }

    return sum;
}

int main(void) {
    char a, b;
    int score = 0;
    while (std::cin >> a >> b) {
        score += score_part_one(a, b);
    }

    std::cout << score << '\n';
    return 0;
}
