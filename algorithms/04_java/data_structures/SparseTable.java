public class SparseTable {
    private int[][] st;
    private int[] log;

    public SparseTable(int[] a) {
        int n = a.length;
        log = new int[n + 1];
        for (int i = 2; i <= n; i++) log[i] = log[i / 2] + 1;
        int k = log[n] + 1;
        st = new int[n][k];
        for (int i = 0; i < n; i++) st[i][0] = a[i];
        for (int j = 1; j < k; j++)
            for (int i = 0; i + (1 << j) <= n; i++)
                st[i][j] = Math.min(st[i][j - 1], st[i + (1 << (j - 1))][j - 1]);
    }

    public int queryMin(int l, int r) {
        int j = log[r - l + 1];
        return Math.min(st[l][j], st[r - (1 << j) + 1][j]);
    }

    public static void main(String[] args) {
        int[] a = {5, 2, 8, 1, 9, 3, 7};
        SparseTable st = new SparseTable(a);
        if (st.queryMin(0, 6) != 1) throw new AssertionError("min(0,6) should be 1");
        if (st.queryMin(0, 2) != 2) throw new AssertionError("min(0,2) should be 2");
        if (st.queryMin(3, 5) != 1) throw new AssertionError("min(3,5) should be 1");
        if (st.queryMin(4, 4) != 9) throw new AssertionError("min(4,4) should be 9");
        System.out.println("[Java SparseTable] O(1) range minimum query verified");
    }
}
