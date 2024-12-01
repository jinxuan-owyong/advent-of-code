#include <iostream>
#include <stack>
#include <vector>

int main(void) {
    // std::vector<std::vector<char>> data = { // sample
    //     {'Z', 'N'},
    //     {'M', 'C', 'D'},
    //     {'P'}};

    std::vector<std::vector<char>> data = {
        {'G', 'F', 'V', 'H', 'P', 'S'},
        {'G', 'J', 'F', 'B', 'V', 'D', 'Z', 'M'},
        {'G', 'M', 'L', 'J', 'N'},
        {'N', 'G', 'Z', 'V', 'D', 'W', 'P'},
        {'V', 'R', 'C', 'B'},
        {'V', 'R', 'S', 'M', 'P', 'W', 'L', 'Z'},
        {'T', 'H', 'P'},
        {'Q', 'R', 'S', 'N', 'C', 'H', 'Z', 'V'},
        {'F', 'L', 'G', 'P', 'V', 'Q', 'J'}};

    std::vector<std::stack<char>> stacks(data.size() + 1, std::stack<char>());
    for (int i = 1; i < data.size() + 1; ++i) {
        for (auto& el : data[i - 1]) stacks[i].emplace(el);
    }

    while (!std::cin.eof()) {
        std::string _;
        int n, src, dest;
        std::cin >> _ >> n >> _ >> src >> _ >> dest;
        if (_.empty())
            break;
        for (int i = 0; i < n; ++i) {
            stacks[dest].push(stacks[src].top());
            stacks[src].pop();
        }
    }

    for (int i = 1; i < data.size() + 1; ++i) {
        if (stacks[i].size() > 0)
            std::cout << stacks[i].top();
    }
    std::cout << '\n';
    return 0;
}
