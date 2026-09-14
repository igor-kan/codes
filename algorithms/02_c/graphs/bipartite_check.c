#include <stdio.h>

#define MAXV 100

int is_bipartite(const int adj[][MAXV], int n) {
    int color[MAXV];
    for (int i = 0; i < n; ++i) color[i] = -1;

    for (int s = 0; s < n; ++s) {
        if (color[s] != -1) continue;
        color[s] = 0;
        int q[MAXV], front = 0, rear = 0;
        q[rear++] = s;
        while (front < rear) {
            int u = q[front++];
            for (int v = 0; v < n; ++v) {
                if (!adj[u][v]) continue;
                if (color[v] == -1) {
                    color[v] = color[u] ^ 1;
                    q[rear++] = v;
                } else if (color[v] == color[u]) {
                    return 0;
                }
            }
        }
    }
    return 1;
}

int main(void) {
    int even[MAXV][MAXV] = {{0}};   /* 4-cycle 0-1-2-3-0 */
    int tri[MAXV][MAXV] = {{0}};    /* triangle 0-1-2-0 */

    int ev[][2] = {{0, 1}, {1, 2}, {2, 3}, {3, 0}};
    int tr[][2] = {{0, 1}, {1, 2}, {2, 0}};
    for (int i = 0; i < 4; ++i) { even[ev[i][0]][ev[i][1]] = even[ev[i][1]][ev[i][0]] = 1; }
    for (int i = 0; i < 3; ++i) { tri[tr[i][0]][tr[i][1]] = tri[tr[i][1]][tr[i][0]] = 1; }

    if (!is_bipartite(even, 4)) {
        printf("[C Bipartite] FAILED: even cycle should be bipartite\n");
        return 1;
    }
    if (is_bipartite(tri, 3)) {
        printf("[C Bipartite] FAILED: triangle should not be bipartite\n");
        return 1;
    }
    printf("[C Bipartite] 2-colorability verified\n");
    return 0;
}
