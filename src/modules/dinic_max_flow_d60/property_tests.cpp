#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_dinic_max_flow_d60;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    DinicFlow df(4);
    df.add_edge(0, 1, 5); df.add_edge(1, 3, 5);
    df.add_edge(0, 2, 5); df.add_edge(2, 3, 5);
    assert(df.max_flow(0, 3) == 10);
    return 0;
}
