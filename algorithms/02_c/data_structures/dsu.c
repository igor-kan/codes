#include <stdio.h>

#define MAXN 1000

typedef struct {
    int parent[MAXN];
    int size[MAXN];
} DSU;

void dsu_init(DSU *d, int n) {
    for (int i = 0; i < n; ++i) {
        d->parent[i] = i;
        d->size[i] = 1;
    }
}

int dsu_find(DSU *d, int x) {
    if (d->parent[x] != x)
        d->parent[x] = dsu_find(d, d->parent[x]);
    return d->parent[x];
}

void dsu_union(DSU *d, int a, int b) {
    int ra = dsu_find(d, a);
    int rb = dsu_find(d, b);
    if (ra == rb) return;
    if (d->size[ra] < d->size[rb]) { int t = ra; ra = rb; rb = t; }
    d->parent[rb] = ra;
    d->size[ra] += d->size[rb];
}

int main(void) {
    DSU d;
    dsu_init(&d, 6);
    dsu_union(&d, 0, 1);
    dsu_union(&d, 1, 2);
    dsu_union(&d, 3, 4);

    if (dsu_find(&d, 0) != dsu_find(&d, 2)) {
        printf("[C DSU] FAILED: transitive connectivity\n");
        return 1;
    }
    if (dsu_find(&d, 0) == dsu_find(&d, 3)) {
        printf("[C DSU] FAILED: false connectivity\n");
        return 1;
    }
    dsu_union(&d, 2, 4);
    if (dsu_find(&d, 0) != dsu_find(&d, 3)) {
        printf("[C DSU] FAILED: merged connectivity\n");
        return 1;
    }
    printf("[C DSU] Union-by-size + path compression verified\n");
    return 0;
}
