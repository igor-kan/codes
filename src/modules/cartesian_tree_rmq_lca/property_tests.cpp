#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_cartesian_tree_rmq_lca;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    std::vector<std::int64_t> a = {5, 4, 3, 2, 1, 6, 7};
    CartesianTree ct(a);
    assert(ct.rmq_index(1, 5) == 4);
    return 0;
}
