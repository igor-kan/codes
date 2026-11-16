#include "interface.hpp"
#include <algorithm>
#include <limits>

namespace codes_li_chao_convex_hull_trick {
Status verify_lichao_oracle(const LiChaoTree& tree, const std::vector<int64_t>& xs) {
    if (tree.inserted.empty()) return Status::NullOrEmpty;
    for (int64_t x : xs) {
        if (x < tree.x_lo || x > tree.x_hi) return Status::OutOfBounds;
        int64_t brute = std::numeric_limits<int64_t>::max();
        for (const auto& fn : tree.inserted) brute = std::min(brute, fn.eval(x));
        if (query_min(tree, x) != brute || query_min_fast(tree, x) != brute) {
            return Status::InvariantViolation;
        }
    }
    return Status::Ok;
}
} // namespace codes_li_chao_convex_hull_trick
