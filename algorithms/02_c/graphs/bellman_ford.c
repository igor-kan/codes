/* Bellman-Ford single-source shortest paths with negative edges. */
#include <stdio.h>
#include <stdbool.h>
#define V 4
#define E 4
#define INF 1000000

bool bellman_ford(int edges[E][3], int src, int dist[V]) {
    for (int i = 0; i < V; i++) dist[i] = INF;
    dist[src] = 0;
    for (int iter = 0; iter < V - 1; iter++)
        for (int e = 0; e < E; e++)
            if (dist[edges[e][0]] != INF &&
                dist[edges[e][0]] + edges[e][2] < dist[edges[e][1]])
                dist[edges[e][1]] = dist[edges[e][0]] + edges[e][2];
    for (int e = 0; e < E; e++)
        if (dist[edges[e][0]] != INF &&
            dist[edges[e][0]] + edges[e][2] < dist[edges[e][1]])
            return false;
    return true;
}

int main(void) {
    int edges[E][3] = {{0, 1, 4}, {0, 2, 5}, {1, 2, -3}, {2, 3, 2}};
    int dist[V];
    if (!bellman_ford(edges, 0, dist)) return 1;
    for (int i = 0; i < V; i++) printf("%d ", dist[i]);
    printf("\n");
    return 0;
}
