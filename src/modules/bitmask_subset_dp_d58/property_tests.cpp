#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_bitmask_subset_dp_d58;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    std::vector<std::vector<long long>> m = {{10, 5}, {3, 8}};
    assert(min_bitmask_assignment(m) <= 18 && min_bitmask_assignment(m) == 8);
    return 0;
}
