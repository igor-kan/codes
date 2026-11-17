#include "interface.hpp"
#include <cassert>
#include <numeric>

int main() {
    using namespace codes_link_cut_tree_splay;
    const int n = 20;
    std::vector<std::int64_t> w(n);
    std::iota(w.begin(), w.end(), 1);
    std::vector<std::pair<int, int>> edges;
    LinkCutTree lct(n);
    for (int i = 0; i < n; ++i) lct.set_value(i, w[static_cast<std::size_t>(i)]);
    for (int i = 0; i + 1 < n; ++i) {
        assert(lct.link(i, i + 1));
        edges.emplace_back(i, i + 1);
    }
    assert(lct.query_path_sum(0, n - 1) == n * (n + 1) / 2);
    auto batch = parallel_forest_path_sums(n, edges, w, {{2, 5}, {3, 10}, {0, 19}});
    assert(batch[0] == 3 + 4 + 5 + 6);
    assert(batch[1] == (11LL * 12) / 2 - 6);
    assert(batch[2] == n * (n + 1) / 2);
    verify_lct_invariants(lct);
    return 0;
}
