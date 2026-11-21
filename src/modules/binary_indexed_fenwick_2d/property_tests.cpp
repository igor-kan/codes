#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_binary_indexed_fenwick_2d;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    Fenwick2D fw(3, 3);
    long long expected = 0;
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            long long val = i * 3 + j + 1;
            fw.add(i, j, val);
            expected += val;
        }
    }
    assert(fw.rect_sum(0, 0, 2, 2) == expected);
    return 0;
}
