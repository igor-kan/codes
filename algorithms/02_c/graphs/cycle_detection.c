#include <stdio.h>

#define MAXV 100

static int visited[MAXV];
static int color[MAXV];

static int dfs_undirected(const int adj[][MAXV], int n, int u, int parent) {
    visited[u] = 1;
    for (int v = 0; v < n; ++v) {
        if (!adj[u][v]) continue;
        if (!visited[v]) {
            if (dfs_undirected(adj, n, v, u)) return 1;
        } else if (v != parent) {
            return 1;
        }
    }
    return 0;
}

int has_cycle_undirected(const int adj[][MAXV], int n) {
    for (int i = 0; i < n; ++i) visited[i] = 0;
    for (int i = 0; i < n; ++i)
        if (!visited[i] && dfs_undirected(adj, n, i, -1)) return 1;
    return 0;
}

static int dfs_directed(const int adj[][MAXV], int n, int u) {
    color[u] = 1;
    for (int v = 0; v < n; ++v) {
        if (!adj[u][v]) continue;
        if (color[v] == 1) return 1;
        if (color[v] == 0 && dfs_directed(adj, n, v)) return 1;
    }
    color[u] = 2;
    return 0;
}

int has_cycle_directed(const int adj[][MAXV], int n) {
    for (int i = 0; i < n; ++i) color[i] = 0;
    for (int i = 0; i < n; ++i)
        if (color[i] == 0 && dfs_directed(adj, n, i)) return 1;
    return 0;
}

int main(void) {
    int u_cycle[MAXV][MAXV] = {{0}};   /* triangle 0-1-2-0 */
    int u_tree[MAXV][MAXV] = {{0}};    /* path 0-1-2 */
    int d_cycle[MAXV][MAXV] = {{0}};   /* 0->1->2->0 */
    int d_dag[MAXV][MAXV] = {{0}};     /* 0->1->2 */

    u_cycle[0][1] = u_cycle[1][0] = 1;
    u_cycle[1][2] = u_cycle[2][1] = 1;
    u_cycle[2][0] = u_cycle[0][2] = 1;

    u_tree[0][1] = u_tree[1][0] = 1;
    u_tree[1][2] = u_tree[2][1] = 1;

    d_cycle[0][1] = d_cycle[1][2] = d_cycle[2][0] = 1;

    d_dag[0][1] = d_dag[1][2] = 1;

    if (!has_cycle_undirected(u_cycle, 3) || has_cycle_undirected(u_tree, 3)) {
        printf("[C CycleDetection] FAILED: undirected\n");
        return 1;
    }
    if (!has_cycle_directed(d_cycle, 3) || has_cycle_directed(d_dag, 3)) {
        printf("[C CycleDetection] FAILED: directed\n");
        return 1;
    }
    printf("[C CycleDetection] Directed + undirected cycle detection verified\n");
    return 0;
}
