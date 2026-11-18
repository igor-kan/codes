#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_dominator_tree_lengauer;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    auto idom = compute_immediate_dominators(5, 0, {{0,1},{1,2},{2,3},{3,4},{1,4}});
    assert(idom[4] == 1 && dominates(idom, 0, 4));
    return 0;
}
