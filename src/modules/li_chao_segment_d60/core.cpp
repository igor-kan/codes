#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_li_chao_segment_d60 {

static constexpr std::int64_t kInfLine = 4000000000000000000LL;
LiChaoTree::LiChaoTree(int lo, int hi)
    : lo_(lo), hi_(hi), tree_(4 * (hi - lo + 1) + 4, LinearFn{0, kInfLine}) {}
void LiChaoTree::insert_rec(int node, int l, int r, LinearFn fn) {
    int mid = l + (r - l) / 2;
    bool left_better = fn.eval(l) < tree_[node].eval(l);
    bool mid_better = fn.eval(mid) < tree_[node].eval(mid);
    if (mid_better) std::swap(tree_[node], fn);
    if (l == r) return;
    if (left_better != mid_better) insert_rec(node * 2, l, mid, fn);
    else insert_rec(node * 2 + 1, mid + 1, r, fn);
}
void LiChaoTree::add_line(std::int64_t m, std::int64_t b) {
    insert_rec(1, lo_, hi_, LinearFn{m, b});
}
std::int64_t LiChaoTree::query_rec(int node, int l, int r, int x) const {
    std::int64_t cur = tree_[node].eval(x);
    if (l == r) return cur;
    int mid = l + (r - l) / 2;
    if (x <= mid) return std::min(cur, query_rec(node * 2, l, mid, x));
    return std::min(cur, query_rec(node * 2 + 1, mid + 1, r, x));
}
std::int64_t LiChaoTree::min_at(int x) const {
    return query_rec(1, lo_, hi_, x);
}

} // namespace codes_li_chao_segment_d60
