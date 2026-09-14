/**
 * Kadane's algorithm: maximum subarray sum.
 */

#include <vector>
#include <algorithm>
#include <cassert>
#include <iostream>

int kadane(const std::vector<int>& a) {
    int best = a[0], cur = a[0];
    for (size_t i = 1; i < a.size(); ++i) {
        cur = std::max(a[i], cur + a[i]);
        best = std::max(best, cur);
    }
    return best;
}

int main() {
    assert(kadane({-2, 1, -3, 4, -1, 2, 1, -5, 4}) == 6);
    assert(kadane({1, 2, 3, 4}) == 10);
    assert(kadane({-1, -2, -3}) == -1);
    assert(kadane({5}) == 5);
    std::cout << "[C++ Kadane] Maximum subarray sum verified." << std::endl;
    return 0;
}
