import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class BridgesArticulation {
    private List<List<Integer>> adj;
    private int[] tin, low;
    private boolean[] visited;
    private int timer;
    private List<int[]> bridges;
    private Set<Integer> articulation;

    public BridgesArticulation(int n) {
        adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        tin = new int[n];
        low = new int[n];
        visited = new boolean[n];
        timer = 0;
        bridges = new ArrayList<>();
        articulation = new HashSet<>();
    }

    public void addEdge(int u, int v) {
        adj.get(u).add(v);
        adj.get(v).add(u);
    }

    public void find(int n) {
        for (int i = 0; i < n; i++)
            if (!visited[i]) dfs(i, -1);
    }

    private void dfs(int v, int p) {
        visited[v] = true;
        tin[v] = low[v] = timer++;
        int children = 0;
        for (int to : adj.get(v)) {
            if (to == p) continue;
            if (visited[to]) {
                low[v] = Math.min(low[v], tin[to]);
            } else {
                dfs(to, v);
                low[v] = Math.min(low[v], low[to]);
                if (low[to] > tin[v]) bridges.add(new int[]{v, to});
                if (low[to] >= tin[v] && p != -1) articulation.add(v);
                children++;
            }
        }
        if (p == -1 && children > 1) articulation.add(v);
    }

    public List<int[]> getBridges() { return bridges; }
    public Set<Integer> getArticulation() { return articulation; }

    public static void main(String[] args) {
        // Triangle 0-1-2-0 plus a dangling bridge 2-3.
        int n = 4;
        BridgesArticulation ba = new BridgesArticulation(n);
        ba.addEdge(0, 1);
        ba.addEdge(1, 2);
        ba.addEdge(2, 0);
        ba.addEdge(2, 3);
        ba.find(n);

        List<int[]> bridges = ba.getBridges();
        boolean found = false;
        for (int[] b : bridges)
            if ((b[0] == 2 && b[1] == 3) || (b[0] == 3 && b[1] == 2)) found = true;
        if (!found) throw new AssertionError("bridge 2-3 should be found");
        if (bridges.size() != 1) throw new AssertionError("exactly one bridge expected, got " + bridges.size());
        if (!ba.getArticulation().contains(2)) throw new AssertionError("node 2 should be articulation point");
        System.out.println("[Java BridgesArticulation] Tarjan bridges/articulation verified");
    }
}
