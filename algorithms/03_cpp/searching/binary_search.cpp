/**
 * Binary search: lower_bound / upper_bound + binary search on answer.
 */

#include <vector>
#include <cassert>
#include <iostream>

int lowerBound(const std::vector<int>& a, int x) {
    int lo = 0, hi = static_cast<int>(a.size());
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (a[mid] < x) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}

int upperBound(const std::vector<int>& a, int x) {
    int lo = 0, hi = static_cast<int>(a.size());
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (a[mid] <= x) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}

// Monotone predicate example: smallest x with x * x >= target.
int sqrtCeil(int target) {
    int lo = 0, hi = target;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (1LL * mid * mid >= target) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}

int main() {
    std::vector<int> a = {1, 2, 2, 3, 3, 3, 5, 7};
    assert(lowerBound(a, 3) == 3);
    assert(upperBound(a, 3) == 6);
    assert(lowerBound(a, 4) == 6);
    assert(upperBound(a, 7) == 8);
    assert(sqrtCeil(17) == 5);
    assert(sqrtCeil(16) == 4);
    std::cout << "[C++ BinarySearch] lower/upper bound and answer search verified." << std::endl;
    return 0;
}
