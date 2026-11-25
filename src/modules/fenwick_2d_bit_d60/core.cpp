#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_fenwick_2d_bit_d60 {

Fenwick2D::Fenwick2D(int r, int c)
    : rows_(r), cols_(c), bit_(r + 1, std::vector<std::int64_t>(c + 1, 0)) {}
void Fenwick2D::add(int r, int c, std::int64_t delta) {
    for (int i = r + 1; i <= rows_; i += i & -i) {
        for (int j = c + 1; j <= cols_; j += j & -j) {
            bit_[i][j] += delta;
        }
    }
}
std::int64_t Fenwick2D::prefix_sum(int r, int c) const {
    if (r < 0 || c < 0) return 0;
    std::int64_t s = 0;
    for (int i = r + 1; i > 0; i -= i & -i) {
        for (int j = c + 1; j > 0; j -= j & -j) {
            s += bit_[i][j];
        }
    }
    return s;
}
std::int64_t Fenwick2D::rect_sum(int r1, int c1, int r2, int c2) const {
    return prefix_sum(r2, c2) - prefix_sum(r1 - 1, c2)
         - prefix_sum(r2, c1 - 1) + prefix_sum(r1 - 1, c1 - 1);
}

} // namespace codes_fenwick_2d_bit_d60
