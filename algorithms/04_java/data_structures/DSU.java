public class DSU {
    private int[] parent;
    private int[] size;

    public DSU(int n) {
        parent = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    public int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }

    public boolean union(int a, int b) {
        int ra = find(a), rb = find(b);
        if (ra == rb) return false;
        if (size[ra] < size[rb]) {
            int tmp = ra; ra = rb; rb = tmp;
        }
        parent[rb] = ra;
        size[ra] += size[rb];
        return true;
    }

    public int sizeOf(int x) {
        return size[find(x)];
    }

    public static void main(String[] args) {
        DSU dsu = new DSU(5);
        dsu.union(0, 1);
        dsu.union(1, 2);
        dsu.union(3, 4);
        if (dsu.find(0) != dsu.find(2)) throw new AssertionError("0 and 2 should be connected");
        if (dsu.find(0) == dsu.find(3)) throw new AssertionError("0 and 3 should be disconnected");
        if (dsu.sizeOf(0) != 3) throw new AssertionError("component size should be 3");
        dsu.union(2, 3);
        if (dsu.find(0) != dsu.find(4)) throw new AssertionError("0 and 4 should now be connected");
        System.out.println("[Java DSU] Union-find with path compression + union by size verified");
    }
}
