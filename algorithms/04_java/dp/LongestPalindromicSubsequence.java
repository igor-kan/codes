public class LongestPalindromicSubsequence {
    public static int lps(String s) {
        int n = s.length();
        if (n == 0) return 0;
        int[][] dp = new int[n][n];
        for (int i = n - 1; i >= 0; i--) {
            dp[i][i] = 1;
            for (int j = i + 1; j < n; j++) {
                if (s.charAt(i) == s.charAt(j)) dp[i][j] = dp[i + 1][j - 1] + 2;
                else dp[i][j] = Math.max(dp[i + 1][j], dp[i][j - 1]);
            }
        }
        return dp[0][n - 1];
    }

    public static void main(String[] args) {
        if (lps("bbbab") != 4) throw new AssertionError("LPS of bbbab should be 4");
        if (lps("cbbd") != 2) throw new AssertionError("LPS of cbbd should be 2");
        if (lps("a") != 1) throw new AssertionError("LPS of a should be 1");
        System.out.println("[Java LongestPalindromicSubsequence] verified: " + lps("bbbab"));
    }
}
