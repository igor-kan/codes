#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_binary_indexed_fenwick_2d {

Fenwick2D::Fenwick2D(int rows, int cols) : rows_(rows), cols_(cols), bit_((rows + 1) * (cols + 1), 0) {
    if (rows <= 0 || cols <= 0) throw std::invalid_argument("positive dimensions required");
}

void Fenwick2D::add(int r, int c, long long delta) {
    if (r < 0 || r >= rows_ || c < 0 || c >= cols_) throw std::out_of_range("cell out of bounds");
    for (int i = r + 1; i <= rows_; i += (i & -i)) {
        for (int j = c + 1; j <= cols_; j += (j & -j)) {
            bit_[i * (cols_ + 1) + j] += delta;
        }
    }
}

long long Fenwick2D::prefix_sum(int r, int c) const {
    if (r < 0 || c < 0) return 0;
    if (r >= rows_) r = rows_ - 1;
    if (c >= cols_) c = cols_ - 1;
    long long s = 0;
    for (int i = r + 1; i > 0; i -= (i & -i)) {
        for (int j = c + 1; j > 0; j -= (j & -j)) {
            s += bit_[i * (cols_ + 1) + j];
        }
    }
    return s;
}

long long Fenwick2D::rect_sum(int r1, int c1, int r2, int c2) const {
    if (r1 > r2 || c1 > c2 || r1 < 0 || c1 < 0 || r2 >= rows_ || c2 >= cols_) {
        throw std::out_of_range("invalid rectangle");
    }
    return prefix_sum(r2, c2) - prefix_sum(r1 - 1, c2) - prefix_sum(r2, c1 - 1) + prefix_sum(r1 - 1, c1 - 1);
}

} // namespace codes_binary_indexed_fenwick_2d
