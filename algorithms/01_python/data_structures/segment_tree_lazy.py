"""Segment tree with lazy propagation for range add + range sum queries."""

from typing import List


class LazySegTree:
    def __init__(self, data: List[int]):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self._build(data, 1, 0, self.n - 1)

    def _build(self, data, node, lo, hi):
        if lo == hi:
            self.tree[node] = data[lo]
            return
        mid = (lo + hi) // 2
        self._build(data, 2 * node, lo, mid)
        self._build(data, 2 * node + 1, mid + 1, hi)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def _push(self, node, lo, hi):
        if self.lazy[node] != 0:
            self.tree[node] += self.lazy[node] * (hi - lo + 1)
            if lo != hi:
                self.lazy[2 * node] += self.lazy[node]
                self.lazy[2 * node + 1] += self.lazy[node]
            self.lazy[node] = 0

    def _update(self, node, lo, hi, ql, qr, val):
        self._push(node, lo, hi)
        if qr < lo or hi < ql:
            return
        if ql <= lo and hi <= qr:
            self.lazy[node] += val
            self._push(node, lo, hi)
            return
        mid = (lo + hi) // 2
        self._update(2 * node, lo, mid, ql, qr, val)
        self._update(2 * node + 1, mid + 1, hi, ql, qr, val)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def _query(self, node, lo, hi, ql, qr):
        self._push(node, lo, hi)
        if qr < lo or hi < ql:
            return 0
        if ql <= lo and hi <= qr:
            return self.tree[node]
        mid = (lo + hi) // 2
        return self._query(2 * node, lo, mid, ql, qr) + self._query(2 * node + 1, mid + 1, hi, ql, qr)

    def update(self, l: int, r: int, val: int):
        self._update(1, 0, self.n - 1, l, r, val)

    def query(self, l: int, r: int) -> int:
        return self._query(1, 0, self.n - 1, l, r)


if __name__ == "__main__":
    st = LazySegTree([1, 2, 3, 4, 5])
    assert st.query(0, 4) == 15
    st.update(1, 3, 10)
    assert st.query(0, 4) == 15 + 30
    assert st.query(1, 3) == 2 + 3 + 4 + 30
    assert st.query(0, 0) == 1
    st.update(0, 4, 5)
    assert st.query(0, 4) == 45 + 25
    print("[Python LazySegTree] Range add + range sum verified.")
