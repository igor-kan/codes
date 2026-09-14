/**
 * Sliding window: fixed-size sum and maximum over a window via monotonic deque.
 */

#include <vector>
#include <deque>
#include <cassert>
#include <iostream>

int maxFixedSum(const std::vector<int>& a, int k) {
    int sum = 0;
    for (int i = 0; i < k; ++i) sum += a[i];
    int best = sum;
    for (int i = k; i < static_cast<int>(a.size()); ++i) {
        sum += a[i] - a[i - k];
        best = std::max(best, sum);
    }
    return best;
}

std::vector<int> slidingWindowMax(const std::vector<int>& a, int k) {
    std::deque<int> dq;
    std::vector<int> res;
    for (int i = 0; i < static_cast<int>(a.size()); ++i) {
        if (!dq.empty() && dq.front() <= i - k) dq.pop_front();
        while (!dq.empty() && a[dq.back()] <= a[i]) dq.pop_back();
        dq.push_back(i);
        if (i >= k - 1) res.push_back(a[dq.front()]);
    }
    return res;
}

int main() {
    std::vector<int> a = {1, 3, -1, -3, 5, 3, 6, 7};
    assert(maxFixedSum(a, 3) == 16);                 // window [3, 6, 7]
    auto maxes = slidingWindowMax(a, 3);
    assert((maxes == std::vector<int>{3, 3, 5, 5, 6, 7}));
    std::cout << "[C++ SlidingWindow] Fixed sum and window maximum verified." << std::endl;
    return 0;
}
