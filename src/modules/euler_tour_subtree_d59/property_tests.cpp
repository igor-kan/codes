#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_euler_tour_subtree_d59;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    auto ss = all_subtree_sums(3, 0, {5, 7, 11}, {{0,1},{1,2}});
    assert(ss[0] == 23 && ss[1] == 18 && ss[2] == 11);
    return 0;
}
