#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_directed_mst_chu_liu;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    std::vector<DirEdge> es = {{0,1,10},{1,2,5},{2,1,4},{2,3,2}};
    assert(edmonds_directed_mst(4, 0, es) == 17);
    return 0;
}
