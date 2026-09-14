#include <stdio.h>

#define MAXN 100000

static long long tree[4 * MAXN];

void seg_build(const long long *a, int node, int l, int r) {
    if (l == r) { tree[node] = a[l]; return; }
    int m = (l + r) / 2;
    seg_build(a, node * 2, l, m);
    seg_build(a, node * 2 + 1, m + 1, r);
    tree[node] = tree[node * 2] + tree[node * 2 + 1];
}

void seg_update(int node, int l, int r, int idx, long long val) {
    if (l == r) { tree[node] = val; return; }
    int m = (l + r) / 2;
    if (idx <= m) seg_update(node * 2, l, m, idx, val);
    else seg_update(node * 2 + 1, m + 1, r, idx, val);
    tree[node] = tree[node * 2] + tree[node * 2 + 1];
}

long long seg_query(int node, int l, int r, int ql, int qr) {
    if (ql > r || qr < l) return 0;
    if (ql <= l && r <= qr) return tree[node];
    int m = (l + r) / 2;
    return seg_query(node * 2, l, m, ql, qr) + seg_query(node * 2 + 1, m + 1, r, ql, qr);
}

int main(void) {
    long long a[] = {1, 2, 3, 4, 5};
    seg_build(a, 1, 0, 4);

    if (seg_query(1, 0, 4, 0, 4) != 15 || seg_query(1, 0, 4, 1, 3) != 9) {
        printf("[C SegmentTree] FAILED: initial query\n");
        return 1;
    }
    seg_update(1, 0, 4, 2, 10);
    if (seg_query(1, 0, 4, 0, 4) != 22 || seg_query(1, 0, 4, 2, 2) != 10) {
        printf("[C SegmentTree] FAILED: post-update query\n");
        return 1;
    }
    printf("[C SegmentTree] Point update + range sum verified\n");
    return 0;
}
