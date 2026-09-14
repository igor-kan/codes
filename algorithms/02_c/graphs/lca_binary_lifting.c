#include <stdio.h>

#define MAXN 100000
#define LOG 17

static int up[LOG][MAXN];
static int depth[MAXN];
static int head[MAXN], to[2 * MAXN], next_e[2 * MAXN];
static int edge_cnt;

static void add_edge(int u, int v) {
    to[edge_cnt] = v; next_e[edge_cnt] = head[u]; head[u] = edge_cnt++;
    to[edge_cnt] = u; next_e[edge_cnt] = head[v]; head[v] = edge_cnt++;
}

static void dfs(int u, int parent) {
    up[0][u] = parent;
    for (int k = 1; k < LOG; ++k)
        up[k][u] = (up[k - 1][u] == -1) ? -1 : up[k - 1][up[k - 1][u]];
    for (int e = head[u]; e != -1; e = next_e[e]) {
        int v = to[e];
        if (v == parent) continue;
        depth[v] = depth[u] + 1;
        dfs(v, u);
    }
}

int lca(int u, int v) {
    if (depth[u] < depth[v]) { int t = u; u = v; v = t; }
    int diff = depth[u] - depth[v];
    for (int k = 0; k < LOG; ++k)
        if (diff & (1 << k)) u = up[k][u];
    if (u == v) return u;
    for (int k = LOG - 1; k >= 0; --k)
        if (up[k][u] != up[k][v]) { u = up[k][u]; v = up[k][v]; }
    return up[0][u];
}

int main(void) {
    edge_cnt = 0;
    for (int i = 0; i < MAXN; ++i) head[i] = -1;

    /* tree: 0 root, 0-1-{3,4}, 0-2-{5,6} */
    add_edge(0, 1);
    add_edge(0, 2);
    add_edge(1, 3);
    add_edge(1, 4);
    add_edge(2, 5);
    add_edge(2, 6);

    depth[0] = 0;
    dfs(0, -1);

    if (lca(3, 4) != 1 || lca(3, 5) != 0 || lca(5, 6) != 2) {
        printf("[C LCA] FAILED: binary lifting mismatch\n");
        return 1;
    }
    printf("[C LCA] Binary lifting LCA verified\n");
    return 0;
}
