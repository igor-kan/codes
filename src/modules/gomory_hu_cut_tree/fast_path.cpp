#include "interface.hpp"
#include <limits>

namespace codes_gomory_hu_cut_tree {
std::vector<std::int64_t> fast_all_pairs_cuts(int n, const std::vector<GhEdge>& tree) {
    std::vector<std::int64_t> mat(static_cast<std::size_t>(n) * static_cast<std::size_t>(n), 0);
    for (int s = 0; s < n; ++s) {
        for (int t = s + 1; t < n; ++t) {
            std::int64_t c = query_pair_min_cut(n, tree, s, t);
            mat[static_cast<std::size_t>(s) * static_cast<std::size_t>(n) + static_cast<std::size_t>(t)] = c;
            mat[static_cast<std::size_t>(t) * static_cast<std::size_t>(n) + static_cast<std::size_t>(s)] = c;
        }
    }
    return mat;
}
} // namespace codes_gomory_hu_cut_tree
