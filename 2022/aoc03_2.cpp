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
        std::string first, second, third;
        std::cin >> first >> second >> third;
        std::set<char> s1, s2, s3, intersect_first, intersect_second;
        for (auto& c : first) s1.insert(c);
        for (auto& c : second) s2.insert(c);
        for (auto& c : third) s3.insert(c);
        std::set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(),
                              std::inserter(intersect_first, intersect_first.begin()));
        std::set_intersection(s3.begin(), s3.end(), intersect_first.begin(), intersect_first.end(),
                              std::inserter(intersect_second, intersect_second.begin()));
        for (auto& c : intersect_second) sum += get_priority(c);
    }

    std::cout << sum << '\n';
    return 0;
}