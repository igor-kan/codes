/**
 * Sparse Table for O(1) range minimum queries after O(n log n) preprocessing.
 */

#include <vector>
#include <algorithm>
#include <cassert>
#include <iostream>

class SparseTable {
    std::vector<std::vector<int>> st;
    std::vector<int> lg;
public:
    explicit SparseTable(const std::vector<int>& a) {
        int n = static_cast<int>(a.size());
        lg.assign(n + 1, 0);
        for (int i = 2; i <= n; ++i) lg[i] = lg[i / 2] + 1;

        int K = lg[n] + 1;
        st.assign(K, std::vector<int>(n));
        st[0] = a;
        for (int k = 1; k < K; ++k) {
            for (int i = 0; i + (1 << k) <= n; ++i) {
                st[k][i] = std::min(st[k - 1][i], st[k - 1][i + (1 << (k - 1))]);
            }
        }
    }

    int query(int l, int r) const { // inclusive [l, r]
        int k = lg[r - l + 1];
        return std::min(st[k][l], st[k][r - (1 << k) + 1]);
    }
};

int main() {
    SparseTable st({1, 3, 2, 7, 9, 11, 5, 2, 8});
    assert(st.query(0, 8) == 1);
    assert(st.query(2, 5) == 2);
    assert(st.query(4, 4) == 9);
    assert(st.query(5, 7) == 2);
    std::cout << "[C++ SparseTable] O(1) RMQ verified." << std::endl;
    return 0;
}
