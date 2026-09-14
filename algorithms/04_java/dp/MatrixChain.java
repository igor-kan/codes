public class MatrixChain {
    public static int matrixChainOrder(int[] dims) {
        int n = dims.length - 1;
        int[][] dp = new int[n][n];
        for (int len = 2; len <= n; len++) {
            for (int i = 0; i + len - 1 < n; i++) {
                int j = i + len - 1;
                dp[i][j] = Integer.MAX_VALUE;
                for (int k = i; k < j; k++) {
                    int cost = dp[i][k] + dp[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1];
                    dp[i][j] = Math.min(dp[i][j], cost);
                }
            }
        }
        return dp[0][n - 1];
    }

    public static void main(String[] args) {
        int[] dims = {10, 30, 5, 60};
        if (matrixChainOrder(dims) != 4500) throw new AssertionError("MCM should be 4500");
        System.out.println("[Java MatrixChain] Matrix chain multiplication verified: " + matrixChainOrder(dims));
    }
}
