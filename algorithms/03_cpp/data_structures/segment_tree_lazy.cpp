/**
 * Segment Tree with lazy propagation supporting range add + range sum.
 */

#include <vector>
#include <cassert>
#include <iostream>

class LazySegTree {
    int n;
    std::vector<long long> tree, lazy;

    void build(const std::vector<long long>& a, int idx, int l, int r) {
        if (l == r) {
            tree[idx] = a[l];
            return;
        }
        int mid = (l + r) / 2;
        build(a, 2 * idx, l, mid);
        build(a, 2 * idx + 1, mid + 1, r);
        tree[idx] = tree[2 * idx] + tree[2 * idx + 1];
    }

    void apply(int idx, int l, int r, long long val) {
        tree[idx] += val * (r - l + 1);
        lazy[idx] += val;
    }

    void push(int idx, int l, int r) {
        if (lazy[idx] == 0) return;
        int mid = (l + r) / 2;
        apply(2 * idx, l, mid, lazy[idx]);
        apply(2 * idx + 1, mid + 1, r, lazy[idx]);
        lazy[idx] = 0;
    }

    void rangeAdd(int idx, int l, int r, int ql, int qr, long long val) {
        if (ql > r || qr < l) return;
        if (ql <= l && r <= qr) {
            apply(idx, l, r, val);
            return;
        }
        push(idx, l, r);
        int mid = (l + r) / 2;
        rangeAdd(2 * idx, l, mid, ql, qr, val);
        rangeAdd(2 * idx + 1, mid + 1, r, ql, qr, val);
        tree[idx] = tree[2 * idx] + tree[2 * idx + 1];
    }

    long long rangeSum(int idx, int l, int r, int ql, int qr) {
        if (ql > r || qr < l) return 0;
        if (ql <= l && r <= qr) return tree[idx];
        push(idx, l, r);
        int mid = (l + r) / 2;
        return rangeSum(2 * idx, l, mid, ql, qr) +
               rangeSum(2 * idx + 1, mid + 1, r, ql, qr);
    }

public:
    explicit LazySegTree(const std::vector<long long>& a) : n(static_cast<int>(a.size())) {
        tree.assign(4 * n, 0);
        lazy.assign(4 * n, 0);
        build(a, 1, 0, n - 1);
    }

    void rangeAdd(int ql, int qr, long long val) {
        rangeAdd(1, 0, n - 1, ql, qr, val);
    }

    long long rangeSum(int ql, int qr) {
        return rangeSum(1, 0, n - 1, ql, qr);
    }
};

int main() {
    LazySegTree seg({1, 2, 3, 4, 5});
    assert(seg.rangeSum(0, 4) == 15);
    seg.rangeAdd(1, 3, 10);
    assert(seg.rangeSum(1, 3) == 39);
    assert(seg.rangeSum(0, 4) == 45);
    seg.rangeAdd(0, 4, 1);
    assert(seg.rangeSum(0, 0) == 2);
    assert(seg.rangeSum(4, 4) == 6);
    std::cout << "[C++ LazySegTree] Range add + range sum verified." << std::endl;
    return 0;
}
