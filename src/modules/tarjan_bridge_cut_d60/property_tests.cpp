#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_tarjan_bridge_cut_d60;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    std::vector<GraphEdge> cycle = {{0,1},{1,2},{2,3},{3,0}};
    auto r = find_bridges_and_cuts(4, cycle);
    assert(r.bridges.empty() && r.cut_vertices.empty());
    return 0;
}
