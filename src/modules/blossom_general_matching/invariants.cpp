#include "interface.hpp"
#include <set>

namespace codes_blossom_general_matching {
void verify_matching_invariants(int n, const std::vector<std::pair<int, int>>& edges, const MatchingResult& res) {
    std::set<std::pair<int, int>> es;
    for (const auto& e : edges) {
        es.emplace(e.first, e.second);
        es.emplace(e.second, e.first);
    }
    int count = 0;
    for (int u = 0; u < n; ++u) {
        int v = res.partner[static_cast<std::size_t>(u)];
        if (v != -1) {
            if (res.partner[static_cast<std::size_t>(v)] != u || !es.count({u, v})) {
                throw std::logic_error("invalid matching symmetry or nonexistent edge");
            }
            ++count;
        }
    }
    if (count != 2 * res.pairs) throw std::logic_error("pair count mismatch");
}
} // namespace codes_blossom_general_matching
