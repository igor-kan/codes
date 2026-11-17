#include "interface.hpp"

namespace codes_link_cut_tree_splay {
void verify_lct_invariants(const LinkCutTree& lct) {
    const auto& raw = lct.raw_nodes();
    for (std::size_t i = 0; i < raw.size(); ++i) {
        for (int s = 0; s < 2; ++s) {
            int c = raw[i].ch[s];
            if (c != -1 && raw[static_cast<std::size_t>(c)].parent != static_cast<int>(i)) {
                throw std::logic_error("broken parent pointer inside splay tree");
            }
        }
    }
}
} // namespace codes_link_cut_tree_splay
