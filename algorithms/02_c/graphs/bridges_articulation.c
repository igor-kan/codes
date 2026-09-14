#include <stdio.h>

#define MAXV 100

static int disc[MAXV], low[MAXV], parent[MAXV], ap_flag[MAXV];
static int timer;

static void dfs(const int adj[][MAXV], int n, int u, int *bridge_count, int *ap_count) {
    disc[u] = low[u] = ++timer;
    int children = 0;
    for (int v = 0; v < n; ++v) {
        if (!adj[u][v]) continue;
        if (disc[v] == 0) {
            parent[v] = u;
            ++children;
            dfs(adj, n, v, bridge_count, ap_count);
            if (low[v] < low[u]) low[u] = low[v];
            if (low[v] > disc[u]) ++(*bridge_count);
            if (parent[u] == -1 && children > 1) {
                if (!ap_flag[u]) { ap_flag[u] = 1; ++(*ap_count); }
            }
            if (parent[u] != -1 && low[v] >= disc[u]) {
                if (!ap_flag[u]) { ap_flag[u] = 1; ++(*ap_count); }
            }
        } else if (v != parent[u]) {
            if (disc[v] < low[u]) low[u] = disc[v];
        }
    }
}

void tarjan(const int adj[][MAXV], int n, int *bridge_count, int *ap_count) {
    timer = 0;
    *bridge_count = 0;
    *ap_count = 0;
    for (int i = 0; i < n; ++i) { disc[i] = 0; parent[i] = -1; ap_flag[i] = 0; }
    for (int i = 0; i < n; ++i)
        if (disc[i] == 0) dfs(adj, n, i, bridge_count, ap_count);
}

int main(void) {
    /* triangle 0-1-2 plus bridge 2-3 */
    int adj[MAXV][MAXV] = {{0}};
    adj[0][1] = adj[1][0] = 1;
    adj[1][2] = adj[2][1] = 1;
    adj[2][0] = adj[0][2] = 1;
    adj[2][3] = adj[3][2] = 1;

    int bridges = 0, aps = 0;
    tarjan(adj, 4, &bridges, &aps);

    if (bridges != 1 || aps != 1) {
        printf("[C Bridges] FAILED: bridges=%d (want 1), articulation=%d (want 1)\n", bridges, aps);
        return 1;
    }
    printf("[C Bridges] Tarjan bridges + articulation points verified\n");
    return 0;
}
