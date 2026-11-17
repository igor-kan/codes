#include "interface.hpp"

namespace codes_blossom_general_matching {
int fast_greedy_warm_match(int n, const std::vector<std::vector<int>>& adj, std::vector<int>& match) {
    int pairs = 0;
    for (int u = 0; u < n; ++u) {
        if (match[static_cast<std::size_t>(u)] != -1) continue;
        for (int v : adj[static_cast<std::size_t>(u)]) {
            if (match[static_cast<std::size_t>(v)] == -1) {
                match[static_cast<std::size_t>(u)] = v;
                match[static_cast<std::size_t>(v)] = u;
                ++pairs;
                break;
            }
        }
    }
    return pairs;
}
} // namespace codes_blossom_general_matching
