/**
 * Hopcroft-Karp in C
 * Maximum bipartite matching.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#define MAXN 100
#define INF 1000000000

int nU, nV;
int adj[MAXN][MAXN], deg[MAXN];
int pairU[MAXN], pairV[MAXN], dist[MAXN];

int bfs(void) {
    int queue[MAXN], head = 0, tail = 0;
    for (int u = 1; u <= nU; u++) {
        if (pairU[u] == 0) {
            dist[u] = 0;
            queue[tail++] = u;
        } else {
            dist[u] = INF;
        }
    }
    dist[0] = INF;

    while (head < tail) {
        int u = queue[head++];
        if (dist[u] < dist[0]) {
            for (int i = 0; i < deg[u]; i++) {
                int v = adj[u][i];
                if (dist[pairV[v]] == INF) {
                    dist[pairV[v]] = dist[u] + 1;
                    queue[tail++] = pairV[v];
                }
            }
        }
    }
    return dist[0] != INF;
}

int dfs(int u) {
    if (u != 0) {
        for (int i = 0; i < deg[u]; i++) {
            int v = adj[u][i];
            if (dist[pairV[v]] == dist[u] + 1 && dfs(pairV[v])) {
                pairV[v] = u;
                pairU[u] = v;
                return 1;
            }
        }
        dist[u] = INF;
        return 0;
    }
    return 1;
}

int hopcroftKarp(void) {
    int matching = 0;
    while (bfs()) {
        for (int u = 1; u <= nU; u++) {
            if (pairU[u] == 0 && dfs(u)) matching++;
        }
    }
    return matching;
}

int main(void) {
    nU = nV = 4;
    deg[1] = 2; adj[1][0] = 2; adj[1][1] = 3;
    deg[2] = 1; adj[2][0] = 1;
    deg[3] = 1; adj[3][0] = 2;
    deg[4] = 2; adj[4][0] = 2; adj[4][1] = 4;
    assert(hopcroftKarp() == 4);
    printf("C Hopcroft-Karp verified.\n");
    return 0;
}
