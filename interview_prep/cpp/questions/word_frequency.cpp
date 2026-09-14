// Count word frequencies with a map and print the top three.
#include <algorithm>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>

int main() {
    std::istringstream stream("the cat the hat the end");
    std::map<std::string, int> counts;
    for (std::string word; stream >> word; ) ++counts[word];

    std::vector<std::pair<std::string, int>> ranked(counts.begin(), counts.end());
    std::sort(ranked.begin(), ranked.end(),
              [](const auto &a, const auto &b) { return a.second > b.second; });

    for (std::size_t i = 0; i < std::min<std::size_t>(3, ranked.size()); ++i)
        std::cout << ranked[i].first << '=' << ranked[i].second << '\n';
    return 0;
}
