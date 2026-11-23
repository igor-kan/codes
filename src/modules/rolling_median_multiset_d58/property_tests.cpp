#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_rolling_median_multiset_d58;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    std::vector<long long> s = {10, 20, 30, 40, 50};
    assert((sliding_window_medians(s, 3) == std::vector<long long>{20, 30, 40}));
    return 0;
}
