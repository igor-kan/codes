#include "interface.hpp"

namespace codes_li_chao_convex_hull_trick {
Status validate_domain(const LiChaoTree& tree, int64_t x) {
    if (tree.nodes.empty() || tree.inserted.empty()) return Status::NullOrEmpty;
    if (x < tree.x_lo || x > tree.x_hi) return Status::OutOfBounds;
    return Status::Ok;
}
} // namespace codes_li_chao_convex_hull_trick
