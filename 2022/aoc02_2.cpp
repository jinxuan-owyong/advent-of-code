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

std::unordered_map<int, int> WINNING_MOVE = {
    {ROCK, PAPER},
    {PAPER, SCISSORS},
    {SCISSORS, ROCK}};

std::unordered_map<int, int> LOSING_MOVE = {
    {ROCK, SCISSORS},
    {PAPER, ROCK},
    {SCISSORS, PAPER}};

int score_part_two(char x, char y) {
    int opp = MOVE[x];
    int sum = 0;

    switch (y) {
    case 'X':
        sum += LOSING_MOVE[opp];
        break;
    case 'Y':
        sum += DRAW;
        sum += opp;
        break;
    case 'Z':
        sum += WIN;
        sum += WINNING_MOVE[opp];
        break;
    }

    return sum;
}

int main(void) {
    char a, b;
    int score = 0;
    while (std::cin >> a >> b) {
        score += score_part_two(a, b);
    }

    std::cout << score << '\n';
    return 0;
}
