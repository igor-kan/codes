#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_zkw_segment_iter_cpp;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    ZkwSegTree st(4); st.point_set(0, 7); st.point_set(3, 5); assert(st.range_sum(0, 3) == 12);
    return 0;
}
