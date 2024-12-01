#include <iostream>
#include <sstream>
#include <vector>
typedef std::pair<int, int> ii;

auto get_pairs(std::string s) {
    std::vector<ii> pairs;
    std::istringstream ss(s);
    std::string first, second;
    std::getline(ss, first, '-');
    std::getline(ss, second, ',');
    pairs.emplace_back(std::pair(stoi(first), stoi(second)));
    std::getline(ss, first, '-');
    std::getline(ss, second);
    pairs.emplace_back(std::pair(stoi(first), stoi(second)));
    return pairs;
}

bool check_ranges(std::vector<ii>& ranges) {  // check fully overlap
    int a = ranges[0].first, b = ranges[0].second;
    int c = ranges[1].first, d = ranges[1].second;
    return ((a >= c && b <= d) || (c >= a && d <= b));
}

int main(void) {
    int count = 0;
    while (!std::cin.eof()) {
        std::string s;
        std::cin >> s;
        if (s.empty())
            break;
        auto ranges = get_pairs(s);
        if (check_ranges(ranges))
            ++count;
    }

    std::cout << count << '\n';
    return 0;
}
