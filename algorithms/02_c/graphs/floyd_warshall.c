/* All-pairs shortest paths (Floyd-Warshall). */
#include <stdio.h>
#define N 4
#define INF 1000000

void floyd_warshall(int dist[N][N]) {
    for (int k = 0; k < N; k++)
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                if (dist[i][k] + dist[k][j] < dist[i][j])
                    dist[i][j] = dist[i][k] + dist[k][j];
}

int main(void) {
    int dist[N][N] = {
        {0, 3, INF, 7},
        {8, 0, 2, INF},
        {5, INF, 0, 1},
        {2, INF, INF, 0},
    };
    floyd_warshall(dist);
    if (dist[0][2] != 5 || dist[0][3] != 6) return 1;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) printf("%d ", dist[i][j]);
        printf("\n");
    }
    return 0;
}
