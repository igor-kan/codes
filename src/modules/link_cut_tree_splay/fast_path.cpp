#include "interface.hpp"

namespace codes_link_cut_tree_splay {
std::vector<bool> fast_connectivity_batch(LinkCutTree& lct, const std::vector<std::pair<int, int>>& pairs) {
    std::vector<bool> out;
    out.reserve(pairs.size());
    for (const auto& p : pairs) {
        out.push_back(lct.connected(p.first, p.second));
    }
    return out;
}
} // namespace codes_link_cut_tree_splay
