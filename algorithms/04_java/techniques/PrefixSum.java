public class PrefixSum {
    public static int[] prefix1D(int[] a) {
        int n = a.length;
        int[] p = new int[n + 1];
        for (int i = 0; i < n; i++) p[i + 1] = p[i] + a[i];
        return p;
    }

    public static int rangeSum1D(int[] p, int l, int r) {
        return p[r + 1] - p[l];
    }

    public static int[][] prefix2D(int[][] g) {
        int m = g.length, n = g[0].length;
        int[][] p = new int[m + 1][n + 1];
        for (int i = 1; i <= m; i++)
            for (int j = 1; j <= n; j++)
                p[i][j] = g[i - 1][j - 1] + p[i - 1][j] + p[i][j - 1] - p[i - 1][j - 1];
        return p;
    }

    public static int rangeSum2D(int[][] p, int r1, int c1, int r2, int c2) {
        return p[r2 + 1][c2 + 1] - p[r1][c2 + 1] - p[r2 + 1][c1] + p[r1][c1];
    }

    public static void main(String[] args) {
        int[] a = {3, 1, 4, 1, 5};
        int[] p1 = prefix1D(a);
        if (rangeSum1D(p1, 1, 3) != 6) throw new AssertionError("1D range sum should be 6");
        int[][] g = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        int[][] p2 = prefix2D(g);
        if (rangeSum2D(p2, 0, 0, 1, 1) != 12) throw new AssertionError("2D sum should be 12");
        if (rangeSum2D(p2, 1, 1, 2, 2) != 28) throw new AssertionError("2D sum should be 28");
        System.out.println("[Java PrefixSum] 1D + 2D prefix sums verified");
    }
}
