#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_zkw_range_sum_d59;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    ZkwSumTree zkw(5);
    for (int i = 0; i < 5; ++i) zkw.add(i, i + 1);
    assert(zkw.sum(0, 4) == 15);
    return 0;
}
