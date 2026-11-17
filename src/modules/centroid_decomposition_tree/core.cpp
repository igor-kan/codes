#include "interface.hpp"
#include <limits>

namespace codes_centroid_decomposition_tree {

static constexpr int INF_DIST = 1'000'000'000;

CentroidOracle::CentroidOracle(int n, const std::vector<std::pair<int, int>>& edges)
    : n_(n), adj_(static_cast<std::size_t>(n)), min_dist_(static_cast<std::size_t>(n), INF_DIST) {
    validate_tree(n, edges);
    for (const auto& e : edges) {
        adj_[static_cast<std::size_t>(e.first)].push_back(e.second);
        adj_[static_cast<std::size_t>(e.second)].push_back(e.first);
    }
    meta_.centroid_parent.assign(static_cast<std::size_t>(n), -1);
    meta_.depth.assign(static_cast<std::size_t>(n), 0);
    meta_.ancestors.resize(static_cast<std::size_t>(n));

    std::vector<bool> blocked(static_cast<std::size_t>(n), false);
    std::vector<int> sub(static_cast<std::size_t>(n), 0);

    auto calc_sub = [&](auto& self, int u, int p) -> int {
        int s = 1;
        for (int v : adj_[static_cast<std::size_t>(u)]) {
            if (v != p && !blocked[static_cast<std::size_t>(v)]) {
                s += self(self, v, u);
            }
        }
        sub[static_cast<std::size_t>(u)] = s;
        return s;
    };

    auto find_cen = [&](auto& self, int u, int p, int tot) -> int {
        for (int v : adj_[static_cast<std::size_t>(u)]) {
            if (v != p && !blocked[static_cast<std::size_t>(v)] && sub[static_cast<std::size_t>(v)] * 2 > tot) {
                return self(self, v, u, tot);
            }
        }
        return u;
    };

    auto collect_dist = [&](auto& self, int u, int p, int d, int cen) -> void {
        meta_.ancestors[static_cast<std::size_t>(u)].emplace_back(cen, d);
        for (int v : adj_[static_cast<std::size_t>(u)]) {
            if (v != p && !blocked[static_cast<std::size_t>(v)]) {
                self(self, v, u, d + 1, cen);
            }
        }
    };

    auto decompose = [&](auto& self, int entry, int p_cen, int dep) -> void {
        int tot = calc_sub(calc_sub, entry, -1);
        int cen = find_cen(find_cen, entry, -1, tot);
        meta_.centroid_parent[static_cast<std::size_t>(cen)] = p_cen;
        meta_.depth[static_cast<std::size_t>(cen)] = dep;
        collect_dist(collect_dist, cen, -1, 0, cen);
        blocked[static_cast<std::size_t>(cen)] = true;
        for (int v : adj_[static_cast<std::size_t>(cen)]) {
            if (!blocked[static_cast<std::size_t>(v)]) {
                self(self, v, cen, dep + 1);
            }
        }
    };
    decompose(decompose, 0, -1, 0);
}

void CentroidOracle::activate(int u) {
    if (u < 0 || u >= n_) throw std::out_of_range("vertex out of range");
    for (const auto& [anc, d] : meta_.ancestors[static_cast<std::size_t>(u)]) {
        if (d < min_dist_[static_cast<std::size_t>(anc)]) {
            min_dist_[static_cast<std::size_t>(anc)] = d;
        }
    }
}

int CentroidOracle::nearest_active_dist(int u) const {
    if (u < 0 || u >= n_) throw std::out_of_range("vertex out of range");
    int best = INF_DIST;
    for (const auto& [anc, d] : meta_.ancestors[static_cast<std::size_t>(u)]) {
        int cand = min_dist_[static_cast<std::size_t>(anc)] + d;
        if (cand < best) best = cand;
    }
    return best >= INF_DIST ? -1 : best;
}

int CentroidOracle::tree_depth() const {
    int mx = 0;
    for (int d : meta_.depth) {
        if (d > mx) mx = d;
    }
    return mx;
}

} // namespace codes_centroid_decomposition_tree
