/**
 * Prefix sums: 1D and 2D.
 */

#include <vector>
#include <cassert>
#include <iostream>

class PrefixSum1D {
    std::vector<long long> pref;
public:
    explicit PrefixSum1D(const std::vector<int>& a) : pref(a.size() + 1, 0) {
        for (size_t i = 0; i < a.size(); ++i) pref[i + 1] = pref[i] + a[i];
    }
    long long sum(int l, int r) const { // inclusive [l, r]
        return pref[r + 1] - pref[l];
    }
};

class PrefixSum2D {
    int rows, cols;
    std::vector<std::vector<long long>> pref;
public:
    PrefixSum2D(const std::vector<std::vector<int>>& a)
        : rows(static_cast<int>(a.size())), cols(static_cast<int>(a[0].size())),
          pref(rows + 1, std::vector<long long>(cols + 1, 0)) {
        for (int i = 1; i <= rows; ++i)
            for (int j = 1; j <= cols; ++j)
                pref[i][j] = a[i - 1][j - 1] + pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1];
    }
    long long sum(int r1, int c1, int r2, int c2) const { // inclusive
        return pref[r2 + 1][c2 + 1] - pref[r1][c2 + 1] - pref[r2 + 1][c1] + pref[r1][c1];
    }
};

int main() {
    PrefixSum1D ps({1, 2, 3, 4, 5});
    assert(ps.sum(0, 4) == 15);
    assert(ps.sum(1, 3) == 9);
    assert(ps.sum(2, 2) == 3);

    PrefixSum2D ps2({{1, 2, 3}, {4, 5, 6}, {7, 8, 9}});
    assert(ps2.sum(0, 0, 2, 2) == 45);
    assert(ps2.sum(1, 1, 2, 2) == 28);
    assert(ps2.sum(0, 0, 0, 0) == 1);
    std::cout << "[C++ PrefixSum] 1D and 2D prefix sums verified." << std::endl;
    return 0;
}
