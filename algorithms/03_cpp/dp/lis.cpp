/**
 * Longest Increasing Subsequence in O(n log n) via patience sorting.
 */

#include <vector>
#include <algorithm>
#include <cassert>
#include <iostream>

int lis(const std::vector<int>& a) {
    std::vector<int> tails;
    for (int x : a) {
        auto it = std::lower_bound(tails.begin(), tails.end(), x);
        if (it == tails.end()) tails.push_back(x);
        else *it = x;
    }
    return static_cast<int>(tails.size());
}

int main() {
    assert(lis({10, 9, 2, 5, 3, 7, 101, 18}) == 4);
    assert(lis({1, 2, 3, 4, 5}) == 5);
    assert(lis({5, 4, 3, 2, 1}) == 1);
    assert(lis({2, 2, 2}) == 1);
    std::cout << "[C++ LIS] Longest increasing subsequence verified." << std::endl;
    return 0;
}
