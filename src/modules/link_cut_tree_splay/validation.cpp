#include "interface.hpp"

namespace codes_link_cut_tree_splay {
void validate_vertex(int n, int v) {
    if (n <= 0 || v < 0 || v >= n) {
        throw std::out_of_range("LinkCutTree vertex index out of bounds");
    }
}
} // namespace codes_link_cut_tree_splay
