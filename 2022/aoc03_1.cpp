#include <algorithm>
#include <iostream>
#include <set>
#include <stack>

int get_priority(char c) {
    if (c >= 'a') {
        return c - 'a' + 1;
    }
    return c - 'A' + 27;
}

int main(void) {
    int sum = 0;

    while (!std::cin.eof()) {
        std::string s;
        std::cin >> s;
        std::set<char> s1, s2, intersect;
        for (int i = 0; i < s.size(); ++i) {
            if (i < s.size() / 2)
                s1.insert(s[i]);
            else
                s2.insert(s[i]);
        }
        std::set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(),
                              std::inserter(intersect, intersect.begin()));
        for (auto& c : intersect) sum += get_priority(c);
    }

    std::cout << sum << '\n';
    return 0;
}