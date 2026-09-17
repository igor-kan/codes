/**
 * Longest Palindromic Subsequence (CLRS 3rd Ed. Chapter 15 Problem 15-2)
 * Computes length of longest subsequence of s that reads the same forward and backward.
 */

export function longestPalindromicSubsequence(s: string): number {
  const n = s.length;
  const dp = Array.from({ length: n }, () => new Array(n).fill(0));

  for (let i = 0; i < n; i++) dp[i][i] = 1;

  for (let len = 2; len <= n; len++) {
    for (let i = 0; i <= n - len; i++) {
      const j = i + len - 1;
      if (s[i] === s[j]) {
        dp[i][j] = dp[i + 1][j - 1] + 2;
      } else {
        dp[i][j] = Math.max(dp[i + 1][j], dp[i][j - 1]);
      }
    }
  }
  return dp[0][n - 1];
}

if (longestPalindromicSubsequence("character") !== 5) {
  throw new Error("Longest Palindromic Subsequence failed");
}
console.log("CLRS Longest Palindromic Subsequence verified successfully.");
