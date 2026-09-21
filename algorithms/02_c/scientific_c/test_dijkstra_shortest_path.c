#include <stdio.h>
#include <assert.h>
#include "dijkstra_shortest_path.h"

int main(void) {
    double graph[MAX_V][MAX_V] = {0};
    graph[0][1] = 4.0;
    graph[0][2] = 1.0;
    graph[2][1] = 2.0;
    double dist[MAX_V];
    dijkstra(graph, 3, 0, dist);
    // Shortest path 0 -> 1 is 0 -> 2 -> 1 with weight 3.0
    assert(dist[1] == 3.0);
    printf("test_dijkstra_shortest_path PASSED\n");
    return 0;
}
