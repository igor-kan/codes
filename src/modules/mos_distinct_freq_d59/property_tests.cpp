#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_mos_distinct_freq_d59;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    auto r = count_equal_pairs_queries({5, 5, 5, 5}, {{0, 3}});
    assert(r[0] == 6);
    return 0;
}
