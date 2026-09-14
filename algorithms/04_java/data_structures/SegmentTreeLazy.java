public class SegmentTreeLazy {
    private long[] tree;
    private long[] lazy;
    private int n;

    public SegmentTreeLazy(int[] arr) {
        n = arr.length;
        tree = new long[4 * n];
        lazy = new long[4 * n];
        build(arr, 1, 0, n - 1);
    }

    private void build(int[] arr, int node, int lo, int hi) {
        if (lo == hi) {
            tree[node] = arr[lo];
            return;
        }
        int mid = (lo + hi) / 2;
        build(arr, node * 2, lo, mid);
        build(arr, node * 2 + 1, mid + 1, hi);
        tree[node] = tree[node * 2] + tree[node * 2 + 1];
    }

    private void push(int node, int lo, int hi) {
        if (lazy[node] != 0) {
            tree[node] += lazy[node] * (hi - lo + 1);
            if (lo != hi) {
                lazy[node * 2] += lazy[node];
                lazy[node * 2 + 1] += lazy[node];
            }
            lazy[node] = 0;
        }
    }

    public void updateRange(int l, int r, int val) {
        updateRange(1, 0, n - 1, l, r, val);
    }

    private void updateRange(int node, int lo, int hi, int l, int r, int val) {
        push(node, lo, hi);
        if (l > hi || r < lo) return;
        if (l <= lo && hi <= r) {
            lazy[node] += val;
            push(node, lo, hi);
            return;
        }
        int mid = (lo + hi) / 2;
        updateRange(node * 2, lo, mid, l, r, val);
        updateRange(node * 2 + 1, mid + 1, hi, l, r, val);
        tree[node] = tree[node * 2] + tree[node * 2 + 1];
    }

    public long queryRange(int l, int r) {
        return queryRange(1, 0, n - 1, l, r);
    }

    private long queryRange(int node, int lo, int hi, int l, int r) {
        push(node, lo, hi);
        if (l > hi || r < lo) return 0;
        if (l <= lo && hi <= r) return tree[node];
        int mid = (lo + hi) / 2;
        return queryRange(node * 2, lo, mid, l, r) + queryRange(node * 2 + 1, mid + 1, hi, l, r);
    }

    public static void main(String[] args) {
        int[] a = {1, 2, 3, 4, 5};
        SegmentTreeLazy seg = new SegmentTreeLazy(a);
        if (seg.queryRange(0, 4) != 15) throw new AssertionError("initial sum should be 15");
        seg.updateRange(1, 3, 2);
        if (seg.queryRange(0, 4) != 21) throw new AssertionError("sum after update should be 21");
        if (seg.queryRange(1, 3) != 15) throw new AssertionError("sum(1,3) should be 15");
        seg.updateRange(0, 4, 10);
        if (seg.queryRange(0, 0) != 11) throw new AssertionError("a[0] should be 11");
        System.out.println("[Java SegmentTreeLazy] Lazy range add + sum query verified");
    }
}
