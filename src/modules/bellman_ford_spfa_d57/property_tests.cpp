#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_bellman_ford_spfa_d57;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    std::vector<DirWeightedEdge> neg_es = {{0, 1, 1}, {1, 2, -2}, {2, 0, -1}};
    assert(bellman_ford_solve(3, 0, neg_es).first);
    return 0;
}
