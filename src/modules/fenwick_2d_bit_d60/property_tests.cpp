#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_fenwick_2d_bit_d60;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    Fenwick2D bit(8, 8);
    std::vector<std::vector<std::int64_t>> g(8, std::vector<std::int64_t>(8, 0));
    for (int k = 0; k < 20; ++k) {
        int r = (k * 3) % 8, c = (k * 5 + 1) % 8;
        std::int64_t d = (k % 5) - 2;
        bit.add(r, c, d);
        g[r][c] += d;
    }
    std::int64_t exact = 0;
    for (int i = 2; i <= 6; ++i)
        for (int j = 1; j <= 5; ++j) exact += g[i][j];
    assert(bit.rect_sum(2, 1, 6, 5) == exact);
    return 0;
}
