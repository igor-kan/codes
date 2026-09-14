import java.util.Arrays;

public final class FloydWarshall {
    private static final int INF = Integer.MAX_VALUE / 2;

    private FloydWarshall() {}

    public static int[][] allPairsShortestPaths(int[][] graph) {
        int n = graph.length;
        int[][] dist = new int[n][n];
        for (int i = 0; i < n; i++) dist[i] = Arrays.copyOf(graph[i], n);
        for (int k = 0; k < n; k++)
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    if (dist[i][k] + dist[k][j] < dist[i][j])
                        dist[i][j] = dist[i][k] + dist[k][j];
        return dist;
    }

    public static void main(String[] args) {
        int[][] graph = {
            {0, 3, INF, 7},
            {8, 0, 2, INF},
            {5, INF, 0, 1},
            {2, INF, INF, 0},
        };
        int[][] dist = allPairsShortestPaths(graph);
        if (dist[0][2] != 5 || dist[0][3] != 6) throw new AssertionError("wrong distance");
        System.out.println(Arrays.toString(dist[0]));
    }
}
