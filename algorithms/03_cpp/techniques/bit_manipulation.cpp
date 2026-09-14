/**
 * Bit manipulation: popcount, lowest set bit, power-of-two and subset enumeration.
 */

#include <vector>
#include <cassert>
#include <iostream>

int popcount(int x) {
    int c = 0;
    while (x) {
        x &= x - 1;
        ++c;
    }
    return c;
}

int lowestSetBit(int x) { return x & -x; }

bool isPowerOfTwo(int x) { return x > 0 && (x & (x - 1)) == 0; }

// Enumerate all subsets of an n-element set as bitmasks.
std::vector<int> allSubsets(int n) {
    std::vector<int> res;
    for (int mask = 0; mask < (1 << n); ++mask) res.push_back(mask);
    return res;
}

// Enumerate all submasks of a given mask (including empty).
std::vector<int> submasks(int mask) {
    std::vector<int> res;
    for (int sub = mask;; sub = (sub - 1) & mask) {
        res.push_back(sub);
        if (sub == 0) break;
    }
    return res;
}

int main() {
    assert(popcount(0b101101) == 4);
    assert(lowestSetBit(12) == 4);       // 1100 -> 0100
    assert(isPowerOfTwo(64));
    assert(!isPowerOfTwo(10));
    assert(allSubsets(3).size() == 8);
    assert(submasks(0b101).size() == 4);
    std::cout << "[C++ BitManipulation] Count, lowbit, power-of-two and subsets verified." << std::endl;
    return 0;
}
