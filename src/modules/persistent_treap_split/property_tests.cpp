#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_persistent_treap_split;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    PersistentTreap pt;
    int r = -1;
    for (int i = 0; i < 10; ++i) r = pt.merge(r, pt.new_node(i + 1, static_cast<std::uint32_t>((i + 3) * 99991u)));
    assert(pt.range_sum(r, 2, 6) == (3 + 4 + 5 + 6 + 7));
    return 0;
}
