#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_dijkstra_minheap_sp;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    std::vector<std::vector<std::pair<int, long long>>> g(3);
    g[0] = {{1, 2}, {2, 10}};
    g[1] = {{2, 3}};
    auto d = dijkstra_distances(3, 0, g);
    assert(d[2] <= d[0] + 10 && d[2] == 5);
    return 0;
}
