#include <iostream>
#include <list>
#include <vector>

int main(void) {
    // std::vector<std::list<char>> data = {// sample
    //                                      {},
    //                                      {'Z', 'N'},
    //                                      {'M', 'C', 'D'},
    //                                      {'P'}};

    std::vector<std::list<char>> data = {
        {},
        {'G', 'F', 'V', 'H', 'P', 'S'},
        {'G', 'J', 'F', 'B', 'V', 'D', 'Z', 'M'},
        {'G', 'M', 'L', 'J', 'N'},
        {'N', 'G', 'Z', 'V', 'D', 'W', 'P'},
        {'V', 'R', 'C', 'B'},
        {'V', 'R', 'S', 'M', 'P', 'W', 'L', 'Z'},
        {'T', 'H', 'P'},
        {'Q', 'R', 'S', 'N', 'C', 'H', 'Z', 'V'},
        {'F', 'L', 'G', 'P', 'V', 'Q', 'J'}};

    while (!std::cin.eof()) {
        std::string _;
        int n, src, dest;
        std::cin >> _ >> n >> _ >> src >> _ >> dest;
        if (_.empty())
            break;

        auto it = data[src].end()--;
        std::advance(it, -n);
        data[dest].splice(data[dest].end(), data[dest], it, data[src].end());
    }

    for (int i = 1; i < data.size(); ++i) {
        if (data[i].size() > 0)
            std::cout << data[i].back();
    }
    std::cout << '\n';
    return 0;
}
