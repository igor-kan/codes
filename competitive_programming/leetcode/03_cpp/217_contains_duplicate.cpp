#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <set>
#include <string>
#include <vector>

bool containsDuplicate(const std::vector<int> &nums) {
    std::set<int> seen;
    for (int value : nums) { if (!seen.insert(value).second) return true; }
    return false;
}

int main() {
    assert(containsDuplicate({1, 2, 3, 1}) && !containsDuplicate({1, 2, 3, 4}));
    std::cout << "217 contains duplicate ok\n";
    return 0;
}
