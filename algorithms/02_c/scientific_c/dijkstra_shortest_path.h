#ifndef DIJKSTRA_SHORTEST_PATH_H
#define DIJKSTRA_SHORTEST_PATH_H

#define MAX_V 32
#define INF_DIST 1e9

void dijkstra(const double graph[MAX_V][MAX_V], int num_v, int src, double dist[MAX_V]);

#endif
