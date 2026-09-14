#include <stdio.h>

#define MAXV 100

int kahn(const int adj[][MAXV], int n, int *indeg, int *order) {
    int q[MAXV], front = 0, rear = 0, idx = 0;
    for (int i = 0; i < n; ++i)
        if (indeg[i] == 0) q[rear++] = i;
    while (front < rear) {
        int u = q[front++];
        order[idx++] = u;
        for (int v = 0; v < n; ++v) {
            if (adj[u][v] && --indeg[v] == 0) q[rear++] = v;
        }
    }
    return idx;
}

int main(void) {
    int adj[MAXV][MAXV] = {{0}};
    int indeg[MAXV] = {0};
    int order[MAXV];

    int edges[][2] = {{5, 2}, {5, 0}, {4, 0}, {4, 1}, {2, 3}, {3, 1}};
    int ne = sizeof(edges) / sizeof(edges[0]);
    for (int i = 0; i < ne; ++i) {
        adj[edges[i][0]][edges[i][1]] = 1;
        ++indeg[edges[i][1]];
    }

    int cnt = kahn(adj, 6, indeg, order);
    if (cnt != 6) {
        printf("[C Kahn] FAILED: processed %d nodes, want 6\n", cnt);
        return 1;
    }
    printf("[C Kahn] Topological sort verified (6 nodes, DAG)\n");
    return 0;
}
