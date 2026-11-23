#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_heavy_light_lca_d58;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    BinaryLiftLca bl(4, 0, {{0,1},{1,2},{2,3}});
    assert(bl.dist(1, 3) == bl.dist(3, 1) && bl.dist(0, 3) == 3);
    return 0;
}
