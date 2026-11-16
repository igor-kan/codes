#include "interface.hpp"
#include <algorithm>
#include <limits>

namespace codes_li_chao_convex_hull_trick {
int64_t query_min_fast(const LiChaoTree& tree, int64_t x) {
    int64_t best = std::numeric_limits<int64_t>::max();
    int idx = 0;
    int64_t l = tree.x_lo, r = tree.x_hi;
    const auto* nodes = tree.nodes.data();
    while (idx >= 0) {
        const auto& nd = nodes[idx];
        if (nd.has_fn) {
            int64_t v = nd.fn.m * x + nd.fn.c;
            if (v < best) best = v;
        }
        if (l == r) break;
        int64_t mid = l + ((r - l) >> 1);
        if (x <= mid) { idx = nd.left; r = mid; }
        else { idx = nd.right; l = mid + 1; }
    }
    return best;
}
} // namespace codes_li_chao_convex_hull_trick
