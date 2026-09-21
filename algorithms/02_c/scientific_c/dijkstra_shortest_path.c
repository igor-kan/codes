#include "dijkstra_shortest_path.h"
#include <stdbool.h>

void dijkstra(const double graph[MAX_V][MAX_V], int num_v, int src, double dist[MAX_V]) {
    bool visited[MAX_V] = {false};
    for (int i = 0; i < num_v; ++i) dist[i] = INF_DIST;
    dist[src] = 0.0;
    
    for (int count = 0; count < num_v - 1; ++count) {
        double min_val = INF_DIST;
        int u = -1;
        for (int v = 0; v < num_v; ++v) {
            if (!visited[v] && dist[v] <= min_val) {
                min_val = dist[v];
                u = v;
            }
        }
        if (u == -1) break;
        visited[u] = true;
        
        for (int v = 0; v < num_v; ++v) {
            if (!visited[v] && graph[u][v] > 0.0 && dist[u] != INF_DIST &&
                dist[u] + graph[u][v] < dist[v]) {
                dist[v] = dist[u] + graph[u][v];
            }
        }
    }
}
