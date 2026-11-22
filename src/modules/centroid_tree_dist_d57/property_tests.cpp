#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_centroid_tree_dist_d57;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    auto ex = compute_tree_extent(4, {{0,1},{1,2},{2,3}});
    assert(ex.diameter == 3 && ex.radius * 2 >= ex.diameter);
    return 0;
}
