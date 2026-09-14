/**
 * Two pointers technique on sorted sequences.
 */

#include <vector>
#include <cassert>
#include <iostream>

bool hasPairSum(const std::vector<int>& a, int target) {
    int l = 0, r = static_cast<int>(a.size()) - 1;
    while (l < r) {
        int s = a[l] + a[r];
        if (s == target) return true;
        if (s < target) ++l;
        else --r;
    }
    return false;
}

int countPairsLessEqual(const std::vector<int>& a, int limit) {
    int l = 0, r = static_cast<int>(a.size()) - 1;
    int count = 0;
    while (l < r) {
        if (a[l] + a[r] <= limit) {
            count += r - l;
            ++l;
        } else {
            --r;
        }
    }
    return count;
}

int main() {
    std::vector<int> a = {1, 2, 3, 4, 5, 7};
    assert(hasPairSum(a, 9));
    assert(!hasPairSum(a, 13));
    assert(hasPairSum(a, 3));
    assert(countPairsLessEqual(a, 6) == 6); // (1,2),(1,3),(1,4),(1,5),(2,3),(2,4)
    std::cout << "[C++ TwoPointers] Pair sum and counting verified." << std::endl;
    return 0;
}
