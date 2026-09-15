// Activity-selection problem (CLRS 16.1).
#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

struct Activity { int start, finish; };

int main() {
    std::vector<Activity> acts{{1, 4}, {3, 5}, {0, 6}, {5, 7}, {3, 9}, {5, 9},
                               {6, 10}, {8, 11}, {8, 12}, {2, 14}, {12, 16}};
    std::sort(acts.begin(), acts.end(),
              [](const Activity &a, const Activity &b) { return a.finish < b.finish; });
    std::vector<Activity> chosen;
    int last = -1;
    for (const auto &a : acts)
        if (a.start >= last) { chosen.push_back(a); last = a.finish; }
    std::vector<std::pair<int, int>> got;
    for (const auto &a : chosen) got.emplace_back(a.start, a.finish);
    assert((got == std::vector<std::pair<int, int>>{{1, 4}, {5, 7}, {8, 11}, {12, 16}}));
    std::cout << "activity selection ok\n";
    return 0;
}
