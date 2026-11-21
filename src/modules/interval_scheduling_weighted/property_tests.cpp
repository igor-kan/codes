#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_interval_scheduling_weighted;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    std::vector<WeightedJob> j = {{0, 4, 15}, {4, 8, 25}, {1, 7, 30}};
    long long best = max_non_overlapping_weight(j);
    assert(best >= 30 && best == 40);
    return 0;
}
