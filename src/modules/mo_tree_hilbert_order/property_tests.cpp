#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_mo_tree_hilbert_order;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    auto res = mo_distinct_queries({5, 5, 5, 5}, {{0, 3}, {1, 2}});
    assert((res == std::vector<int>{1, 1}));
    return 0;
}
