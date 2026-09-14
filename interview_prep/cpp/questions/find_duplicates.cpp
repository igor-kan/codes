// Find the first duplicate in a vector using a set.
#include <cassert>
#include <iostream>
#include <optional>
#include <unordered_set>
#include <vector>

std::optional<int> first_duplicate(const std::vector<int> &values) {
    std::unordered_set<int> seen;
    for (int value : values)
        if (!seen.insert(value).second) return value;
    return std::nullopt;
}

int main() {
    assert(first_duplicate({1, 3, 4, 3, 2}).value() == 3);
    assert(!first_duplicate({1, 2, 3}).has_value());
    std::cout << "ok\n";
    return 0;
}
