#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_dinic_scaling_maxflow;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    ScalingDinic g(6);
    g.add_edge(0, 1, 16); g.add_edge(0, 2, 13);
    g.add_edge(1, 2, 10); g.add_edge(1, 3, 12);
    g.add_edge(2, 1, 4);  g.add_edge(2, 4, 14);
    g.add_edge(3, 2, 9);  g.add_edge(3, 5, 20);
    g.add_edge(4, 3, 7);  g.add_edge(4, 5, 4);
    assert(g.max_flow(0, 5) == 23);
    return 0;
}
