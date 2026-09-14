#include <stdio.h>

#define MAXV 100

static void reverse(int *a, int len) {
    for (int i = 0, j = len - 1; i < j; ++i, --j) {
        int t = a[i]; a[i] = a[j]; a[j] = t;
    }
}

/* Hierholzer's algorithm for a directed Eulerian circuit. Mutates adj. */
int hierholzer(int adj[][MAXV], int n, int start, int *path) {
    int stack[MAXV * MAXV], top = -1;
    int len = 0;
    stack[++top] = start;
    while (top >= 0) {
        int u = stack[top];
        int found = -1;
        for (int v = 0; v < n; ++v)
            if (adj[u][v]) { found = v; break; }
        if (found != -1) {
            adj[u][found] = 0;
            stack[++top] = found;
        } else {
            path[len++] = stack[top--];
        }
    }
    reverse(path, len);
    return len;
}

int main(void) {
    /* directed 4-cycle 0->1->2->3->0 forms an Eulerian circuit */
    int adj[MAXV][MAXV] = {{0}};
    adj[0][1] = 1; adj[1][2] = 1; adj[2][3] = 1; adj[3][0] = 1;

    int path[MAXV * MAXV];
    int len = hierholzer(adj, 4, 0, path);

    if (len != 5 || path[0] != 0 || path[len - 1] != 0) {
        printf("[C EulerianPath] FAILED: circuit length %d\n", len);
        return 1;
    }
    printf("[C EulerianPath] Hierholzer Eulerian circuit verified\n");
    return 0;
}
