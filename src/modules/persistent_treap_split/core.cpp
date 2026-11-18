#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_persistent_treap_split {

int PersistentTreap::new_node(std::int64_t val, std::uint32_t prio) {
    int id = static_cast<int>(pool_.size());
    pool_.push_back(PTreapNode{val, val, prio, 1, -1, -1});
    return id;
}

int PersistentTreap::clone_node(int u) {
    if (u < 0) return -1;
    int id = static_cast<int>(pool_.size());
    pool_.push_back(pool_[u]);
    return id;
}

void PersistentTreap::pull(int u) {
    if (u < 0) return;
    int l = pool_[u].l, r = pool_[u].r;
    pool_[u].sz = 1 + size_of(l) + size_of(r);
    pool_[u].sum = pool_[u].val + (l < 0 ? 0 : pool_[l].sum) + (r < 0 ? 0 : pool_[r].sum);
}

std::pair<int, int> PersistentTreap::split(int root, int k) {
    if (root < 0) return {-1, -1};
    int cur = clone_node(root);
    int lsz = size_of(pool_[cur].l);
    if (k <= lsz) {
        auto [ll, lr] = split(pool_[cur].l, k);
        pool_[cur].l = lr;
        pull(cur);
        return {ll, cur};
    } else {
        auto [rl, rr] = split(pool_[cur].r, k - lsz - 1);
        pool_[cur].r = rl;
        pull(cur);
        return {cur, rr};
    }
}

int PersistentTreap::merge(int a, int b) {
    if (a < 0) return b;
    if (b < 0) return a;
    if (pool_[a].prio > pool_[b].prio) {
        int cur = clone_node(a);
        pool_[cur].r = merge(pool_[cur].r, b);
        pull(cur);
        return cur;
    } else {
        int cur = clone_node(b);
        pool_[cur].l = merge(a, pool_[cur].l);
        pull(cur);
        return cur;
    }
}

std::int64_t PersistentTreap::range_sum(int root, int l, int r) {
    auto [t1, t2] = split(root, r + 1);
    auto [t1a, t1b] = split(t1, l);
    return t1b < 0 ? 0 : pool_[t1b].sum;
}

} // namespace codes_persistent_treap_split
