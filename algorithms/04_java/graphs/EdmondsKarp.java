import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;

public final class EdmondsKarp {
    private EdmondsKarp() {}

    public static int maxFlow(int[][] capacity, int source, int sink) {
        int n = capacity.length;
        int[][] residual = new int[n][];
        for (int i = 0; i < n; i++) {
            residual[i] = capacity[i].clone();
        }
        int flow = 0;
        while (true) {
            int[] parent = new int[n];
            Arrays.fill(parent, -1);
            parent[source] = source;
            Queue<Integer> queue = new ArrayDeque<>();
            queue.add(source);
            while (!queue.isEmpty() && parent[sink] == -1) {
                int u = queue.poll();
                for (int v = 0; v < n; v++) {
                    if (parent[v] == -1 && residual[u][v] > 0) {
                        parent[v] = u;
                        queue.add(v);
                    }
                }
            }
            if (parent[sink] == -1) {
                break;
            }
            int bottleneck = Integer.MAX_VALUE;
            for (int v = sink; v != source; v = parent[v]) {
                bottleneck = Math.min(bottleneck, residual[parent[v]][v]);
            }
            for (int v = sink; v != source; v = parent[v]) {
                residual[parent[v]][v] -= bottleneck;
                residual[v][parent[v]] += bottleneck;
            }
            flow += bottleneck;
        }
        return flow;
    }

    public static void main(String[] args) {
        int[][] capacity = {
            {0, 16, 13, 0, 0, 0}, {0, 0, 10, 12, 0, 0}, {0, 4, 0, 0, 14, 0},
            {0, 0, 9, 0, 0, 20}, {0, 0, 0, 7, 0, 4}, {0, 0, 0, 0, 0, 0},
        };
        if (maxFlow(capacity, 0, 5) != 23) {
            throw new AssertionError("wrong flow");
        }
        System.out.println("edmonds-karp ok");
    }
}
