#include "interface.hpp"
#include <algorithm>
#include <limits>

namespace codes_li_chao_convex_hull_trick {
LiChaoTree make_lichao_tree(int64_t lo, int64_t hi) {
    LiChaoTree t;
    t.x_lo = lo;
    t.x_hi = hi;
    t.nodes.push_back(LiChaoNode{});
    return t;
}

static void insert_rec(LiChaoTree& t, int idx, int64_t l, int64_t r, LineFn nw) {
    if (!t.nodes[static_cast<std::size_t>(idx)].has_fn) {
        t.nodes[static_cast<std::size_t>(idx)].fn = nw;
        t.nodes[static_cast<std::size_t>(idx)].has_fn = true;
        return;
    }
    int64_t mid = l + (r - l) / 2;
    bool left_better = nw.eval(l) < t.nodes[static_cast<std::size_t>(idx)].fn.eval(l);
    bool mid_better = nw.eval(mid) < t.nodes[static_cast<std::size_t>(idx)].fn.eval(mid);
    if (mid_better) {
        std::swap(t.nodes[static_cast<std::size_t>(idx)].fn, nw);
    }
    if (l == r) return;
    if (left_better != mid_better) {
        if (t.nodes[static_cast<std::size_t>(idx)].left == -1) {
            t.nodes[static_cast<std::size_t>(idx)].left = static_cast<int>(t.nodes.size());
            t.nodes.push_back(LiChaoNode{});
        }
        insert_rec(t, t.nodes[static_cast<std::size_t>(idx)].left, l, mid, nw);
    } else {
        if (t.nodes[static_cast<std::size_t>(idx)].right == -1) {
            t.nodes[static_cast<std::size_t>(idx)].right = static_cast<int>(t.nodes.size());
            t.nodes.push_back(LiChaoNode{});
        }
        insert_rec(t, t.nodes[static_cast<std::size_t>(idx)].right, mid + 1, r, nw);
    }
}

Status insert_line(LiChaoTree& tree, LineFn fn) {
    if (tree.nodes.empty() || tree.x_lo > tree.x_hi) return Status::InvalidInput;
    tree.inserted.push_back(fn);
    insert_rec(tree, 0, tree.x_lo, tree.x_hi, fn);
    return Status::Ok;
}

int64_t query_min(const LiChaoTree& tree, int64_t x) {
    int64_t ans = std::numeric_limits<int64_t>::max();
    int idx = 0;
    int64_t l = tree.x_lo, r = tree.x_hi;
    while (idx != -1) {
        const auto& nd = tree.nodes[static_cast<std::size_t>(idx)];
        if (nd.has_fn) ans = std::min(ans, nd.fn.eval(x));
        if (l == r) break;
        int64_t mid = l + (r - l) / 2;
        if (x <= mid) { idx = nd.left; r = mid; }
        else { idx = nd.right; l = mid + 1; }
    }
    return ans;
}
} // namespace codes_li_chao_convex_hull_trick
