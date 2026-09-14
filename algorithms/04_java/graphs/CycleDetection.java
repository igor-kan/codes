import java.util.ArrayList;
import java.util.List;

public class CycleDetection {
    // Directed graph cycle detection via DFS colors: 0 = unvisited, 1 = in stack, 2 = done.
    public static boolean hasCycleDirected(int n, List<List<Integer>> adj) {
        int[] state = new int[n];
        for (int s = 0; s < n; s++)
            if (state[s] == 0 && dfsDirected(s, adj, state)) return true;
        return false;
    }

    private static boolean dfsDirected(int u, List<List<Integer>> adj, int[] state) {
        state[u] = 1;
        for (int v : adj.get(u)) {
            if (state[v] == 1) return true;
            if (state[v] == 0 && dfsDirected(v, adj, state)) return true;
        }
        state[u] = 2;
        return false;
    }

    // Undirected graph cycle detection via DFS parent.
    public static boolean hasCycleUndirected(int n, List<List<Integer>> adj) {
        boolean[] visited = new boolean[n];
        for (int s = 0; s < n; s++)
            if (!visited[s] && dfsUndirected(s, -1, adj, visited)) return true;
        return false;
    }

    private static boolean dfsUndirected(int u, int parent, List<List<Integer>> adj, boolean[] visited) {
        visited[u] = true;
        for (int v : adj.get(u)) {
            if (!visited[v]) {
                if (dfsUndirected(v, u, adj, visited)) return true;
            } else if (v != parent) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        List<List<Integer>> dg = new ArrayList<>();
        for (int i = 0; i < 3; i++) dg.add(new ArrayList<>());
        dg.get(0).add(1); dg.get(1).add(2); dg.get(2).add(0);
        if (!hasCycleDirected(3, dg)) throw new AssertionError("directed cycle should be detected");

        List<List<Integer>> dag = new ArrayList<>();
        for (int i = 0; i < 3; i++) dag.add(new ArrayList<>());
        dag.get(0).add(1); dag.get(0).add(2); dag.get(1).add(2);
        if (hasCycleDirected(3, dag)) throw new AssertionError("DAG should have no cycle");

        List<List<Integer>> ug = new ArrayList<>();
        for (int i = 0; i < 3; i++) ug.add(new ArrayList<>());
        ug.get(0).add(1); ug.get(1).add(0);
        ug.get(1).add(2); ug.get(2).add(1);
        ug.get(2).add(0); ug.get(0).add(2);
        if (!hasCycleUndirected(3, ug)) throw new AssertionError("undirected cycle should be detected");
        System.out.println("[Java CycleDetection] Cycle detection (directed + undirected) verified");
    }
}
