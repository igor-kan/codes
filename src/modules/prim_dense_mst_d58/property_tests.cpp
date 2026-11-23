#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_prim_dense_mst_d58;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    std::vector<std::vector<long long>> u = {{0, 5, 5}, {5, 0, 5}, {5, 5, 0}};
    assert(prim_dense_mst(u) == 10);
    return 0;
}
