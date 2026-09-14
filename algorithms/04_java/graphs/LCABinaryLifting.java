import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class LCABinaryLifting {
    private int LOG;
    private int[] depth;
    private int[][] up;
    private List<List<Integer>> adj;

    public LCABinaryLifting(int n, List<List<Integer>> adj, int root) {
        this.adj = adj;
        LOG = 32 - Integer.numberOfLeadingZeros(n);
        depth = new int[n];
        up = new int[n][LOG];
        for (int[] row : up) Arrays.fill(row, -1);
        build(root, -1);
    }

    private void build(int u, int p) {
        up[u][0] = p;
        for (int k = 1; k < LOG; k++) {
            int mid = up[u][k - 1];
            up[u][k] = mid == -1 ? -1 : up[mid][k - 1];
        }
        for (int v : adj.get(u)) {
            if (v != p) {
                depth[v] = depth[u] + 1;
                build(v, u);
            }
        }
    }

    public int lca(int a, int b) {
        if (depth[a] < depth[b]) { int t = a; a = b; b = t; }
        int diff = depth[a] - depth[b];
        for (int k = 0; k < LOG; k++)
            if ((diff & (1 << k)) != 0) a = up[a][k];
        if (a == b) return a;
        for (int k = LOG - 1; k >= 0; k--) {
            if (up[a][k] != up[b][k]) {
                a = up[a][k];
                b = up[b][k];
            }
        }
        return up[a][0];
    }

    public static void main(String[] args) {
        int n = 7;
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        adj.get(0).add(1); adj.get(1).add(0);
        adj.get(0).add(2); adj.get(2).add(0);
        adj.get(1).add(3); adj.get(3).add(1);
        adj.get(1).add(4); adj.get(4).add(1);
        adj.get(2).add(5); adj.get(5).add(2);
        adj.get(2).add(6); adj.get(6).add(2);
        LCABinaryLifting lca = new LCABinaryLifting(n, adj, 0);
        if (lca.lca(3, 4) != 1) throw new AssertionError("lca(3,4) should be 1");
        if (lca.lca(3, 6) != 0) throw new AssertionError("lca(3,6) should be 0");
        if (lca.lca(5, 6) != 2) throw new AssertionError("lca(5,6) should be 2");
        if (lca.lca(1, 3) != 1) throw new AssertionError("lca(1,3) should be 1");
        System.out.println("[Java LCABinaryLifting] Lowest common ancestor verified");
    }
}
