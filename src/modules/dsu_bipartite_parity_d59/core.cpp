#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_dsu_bipartite_parity_d59 {

BipartiteDsu::BipartiteDsu(int n) : p_(n), col_(n, 0) {
    for (int i = 0; i < n; ++i) p_[i] = i;
}

std::pair<int, int> BipartiteDsu::find(int x) {
    if (p_[x] == x) return {x, 0};
    auto [root, c] = find(p_[x]);
    p_[x] = root;
    col_[x] ^= c;
    return {p_[x], col_[x]};
}

bool BipartiteDsu::add_edge(int u, int v) {
    auto [ru, cu] = find(u);
    auto [rv, cv] = find(v);
    if (ru == rv) {
        if (cu == cv) ok_ = false;
    } else {
        p_[rv] = ru;
        col_[rv] = cu ^ cv ^ 1;
    }
    return ok_;
}

} // namespace codes_dsu_bipartite_parity_d59
