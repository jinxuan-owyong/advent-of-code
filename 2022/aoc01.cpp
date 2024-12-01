#include <iostream>
#include <set>

int main(void) {
    std::set<int> calories;
    int sum = 0;
    std::string s;
    while (!std::cin.eof()) {
        std::getline(std::cin, s);
        if (s.empty()) {
            calories.insert(sum);
            sum = 0;
            continue;
        }

        sum += std::stoi(s);
    }

    auto it = --calories.end();
    int first = *it--;
    int second = *it--;
    int third = *it--;

    std::cout << first << '\n';
    std::cout << second << '\n';
    std::cout << third << '\n';
    std::cout << first + second + third << '\n';
}
