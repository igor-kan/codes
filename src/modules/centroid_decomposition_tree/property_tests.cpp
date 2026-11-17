#include "interface.hpp"
#include <cassert>
#include <queue>

int main() {
    using namespace codes_centroid_decomposition_tree;
    const int n = 31;
    std::vector<std::pair<int, int>> edges;
    for (int i = 1; i < n; ++i) edges.emplace_back((i - 1) / 2, i);
    auto ans = parallel_multi_query(n, edges, {0, 15, 28}, {30, 14, 15, 29, 7});
    assert(ans[0] == 4);
    assert(ans[1] == 3);
    assert(ans[2] == 0);
    assert(ans[3] == 4);
    assert(ans[4] == 1);
    return 0;
}
