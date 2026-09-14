import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Deque;
import java.util.List;

public class MaxFlowDinic {
    static class Edge {
        int to, rev;
        long cap;
        Edge(int to, long cap, int rev) { this.to = to; this.cap = cap; this.rev = rev; }
    }

    private List<Edge>[] g;
    private int[] level, it;

    @SuppressWarnings("unchecked")
    public MaxFlowDinic(int n) {
        g = new List[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        level = new int[n];
        it = new int[n];
    }

    public void addEdge(int u, int v, long cap) {
        g[u].add(new Edge(v, cap, g[v].size()));
        g[v].add(new Edge(u, 0, g[u].size() - 1));
    }

    private boolean bfs(int s, int t) {
        Arrays.fill(level, -1);
        Deque<Integer> q = new ArrayDeque<>();
        level[s] = 0;
        q.add(s);
        while (!q.isEmpty()) {
            int u = q.poll();
            for (Edge e : g[u]) {
                if (e.cap > 0 && level[e.to] == -1) {
                    level[e.to] = level[u] + 1;
                    q.add(e.to);
                }
            }
        }
        return level[t] != -1;
    }

    private long dfs(int u, int t, long f) {
        if (u == t) return f;
        for (; it[u] < g[u].size(); it[u]++) {
            Edge e = g[u].get(it[u]);
            if (e.cap > 0 && level[e.to] == level[u] + 1) {
                long d = dfs(e.to, t, Math.min(f, e.cap));
                if (d > 0) {
                    e.cap -= d;
                    g[e.to].get(e.rev).cap += d;
                    return d;
                }
            }
        }
        return 0;
    }

    public long maxFlow(int s, int t) {
        long flow = 0;
        while (bfs(s, t)) {
            Arrays.fill(it, 0);
            long f;
            while ((f = dfs(s, t, Long.MAX_VALUE)) > 0) flow += f;
        }
        return flow;
    }

    public static void main(String[] args) {
        MaxFlowDinic dinic = new MaxFlowDinic(6);
        dinic.addEdge(0, 1, 16);
        dinic.addEdge(0, 2, 13);
        dinic.addEdge(1, 2, 10);
        dinic.addEdge(1, 3, 12);
        dinic.addEdge(2, 1, 4);
        dinic.addEdge(2, 4, 14);
        dinic.addEdge(3, 2, 9);
        dinic.addEdge(3, 5, 20);
        dinic.addEdge(4, 3, 7);
        dinic.addEdge(4, 5, 4);
        long flow = dinic.maxFlow(0, 5);
        if (flow != 23) throw new AssertionError("max flow should be 23, got " + flow);
        System.out.println("[Java MaxFlowDinic] Dinic's max flow verified: " + flow);
    }
}
