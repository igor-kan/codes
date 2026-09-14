import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

public class KahnTopologicalSort {
    public static List<Integer> topologicalSort(int n, List<List<Integer>> adj) {
        int[] indegree = new int[n];
        for (int u = 0; u < n; u++)
            for (int v : adj.get(u)) indegree[v]++;
        Deque<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < n; i++) if (indegree[i] == 0) q.add(i);
        List<Integer> order = new ArrayList<>();
        while (!q.isEmpty()) {
            int u = q.poll();
            order.add(u);
            for (int v : adj.get(u))
                if (--indegree[v] == 0) q.add(v);
        }
        if (order.size() != n) return null;
        return order;
    }

    public static void main(String[] args) {
        int n = 6;
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        adj.get(5).add(2);
        adj.get(5).add(0);
        adj.get(4).add(0);
        adj.get(4).add(1);
        adj.get(2).add(3);
        adj.get(3).add(1);
        List<Integer> order = topologicalSort(n, adj);
        if (order == null) throw new AssertionError("graph should be a DAG");
        int[] pos = new int[n];
        for (int i = 0; i < order.size(); i++) pos[order.get(i)] = i;
        for (int u = 0; u < n; u++)
            for (int v : adj.get(u))
                if (pos[u] >= pos[v]) throw new AssertionError("edge " + u + "->" + v + " violates order");
        System.out.println("[Java KahnTopologicalSort] Kahn's algorithm verified: " + order);
    }
}
