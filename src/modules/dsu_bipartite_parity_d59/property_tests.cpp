#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_dsu_bipartite_parity_d59;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    BipartiteDsu tri(3);
    assert(tri.add_edge(0, 1) && tri.add_edge(1, 2) && !tri.add_edge(2, 0));
    return 0;
}
