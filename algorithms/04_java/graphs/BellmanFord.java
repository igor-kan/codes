import java.util.Arrays;

public final class BellmanFord {
    private static final long INF = Long.MAX_VALUE / 4;

    private BellmanFord() {}

    public record Edge(int from, int to, int weight) {}

    public static long[] shortestPaths(int nodes, Edge[] edges, int source) {
        long[] dist = new long[nodes];
        Arrays.fill(dist, INF);
        dist[source] = 0;
        for (int i = 0; i < nodes - 1; i++)
            for (Edge e : edges)
                if (dist[e.from()] != INF && dist[e.from()] + e.weight() < dist[e.to()])
                    dist[e.to()] = dist[e.from()] + e.weight();
        for (Edge e : edges)
            if (dist[e.from()] != INF && dist[e.from()] + e.weight() < dist[e.to()])
                throw new IllegalStateException("negative cycle");
        return dist;
    }

    public static void main(String[] args) {
        Edge[] edges = {
            new Edge(0, 1, 4),
            new Edge(0, 2, 5),
            new Edge(1, 2, -3),
            new Edge(2, 3, 2),
        };
        long[] dist = shortestPaths(4, edges, 0);
        if (!Arrays.equals(dist, new long[] {0, 4, 1, 3})) throw new AssertionError("wrong distance");
        System.out.println(Arrays.toString(dist));
    }
}
