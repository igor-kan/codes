// Greedy set cover (CLRS 35.3).
#include <cassert>
#include <iostream>
#include <set>
#include <vector>

std::vector<std::set<int>> setCover(std::set<int> universe, const std::vector<std::set<int>> &subsets) {
    std::vector<std::set<int>> chosen;
    while (!universe.empty()) {
        const std::set<int> *best = nullptr;
        size_t bestCount = 0;
        for (const auto &subset : subsets) {
            size_t count = 0;
            for (int value : subset) if (universe.count(value)) ++count;
            if (count > bestCount) { bestCount = count; best = &subset; }
        }
        if (!best || bestCount == 0) break;
        chosen.push_back(*best);
        for (int value : *best) universe.erase(value);
    }
    return chosen;
}

int main() {
    std::vector<std::set<int>> subsets{{1, 2, 3}, {2, 4}, {3, 4}, {4, 5}};
    auto chosen = setCover({1, 2, 3, 4, 5}, subsets);
    assert(chosen.size() == 2);
    std::cout << "set cover ok\n";
    return 0;
}
