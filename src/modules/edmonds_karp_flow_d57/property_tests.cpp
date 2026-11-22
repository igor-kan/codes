#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_edmonds_karp_flow_d57;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    std::vector<FlowEdgeSpec> diamond = {{0,1,5},{0,2,5},{1,3,3},{2,3,7}};
    assert(edmonds_karp_maxflow(4, 0, 3, diamond) == 8);
    return 0;
}
