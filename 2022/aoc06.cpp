#include <iostream>
#include <vector>

// const int N_DISTINCT = 4;
const int N_DISTINCT = 14;

int main(void) {
    std::vector<char> s;  // input string
    while (!std::cin.eof()) {
        char c;
        std::cin >> c;
        s.emplace_back(c);
    }

    for (int i = 0; i < s.size() - N_DISTINCT; ++i) {  // O(N)
        std::vector<int> count(26, 0);
        int sum = 0;
        for (int j = i; j < i + N_DISTINCT; ++j) {
            int id = s[j] - 'a';
            if (count[id] != 0) {  // repeated character
                break;
            }
            ++count[id];
            ++sum;
        }
        if (sum == N_DISTINCT) {
            std::cout << i + N_DISTINCT << '\n';  // 1-based indexing
            return 0;
        }
    }

    return 0;
}