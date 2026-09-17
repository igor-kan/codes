/**
 * Subset Sum Problem (CLRS 3rd Ed. Chapter 35.5 NP-completeness)
 * Pseudo-polynomial time dynamic programming O(n * sum) with item recovery.
 */

export function subsetSum(arr: number[], target: number): number[] | null {
  const n = arr.length;
  const dp = Array.from({ length: n + 1 }, () => new Array(target + 1).fill(false));
  for (let i = 0; i <= n; i++) dp[i][0] = true;

  for (let i = 1; i <= n; i++) {
    const val = arr[i - 1];
    for (let s = 1; s <= target; s++) {
      if (val <= s) {
        dp[i][s] = dp[i - 1][s] || dp[i - 1][s - val];
      } else {
        dp[i][s] = dp[i - 1][s];
      }
    }
  }

  if (!dp[n][target]) return null;

  const subset: number[] = [];
  let curS = target;
  for (let i = n; i > 0 && curS > 0; i--) {
    if (!dp[i - 1][curS]) {
      subset.push(arr[i - 1]);
      curS -= arr[i - 1];
    }
  }
  return subset;
}

const ssRes = subsetSum([3, 34, 4, 12, 5, 2], 9);
if (!ssRes || ssRes.reduce((a, b) => a + b, 0) !== 9) throw new Error("Subset Sum failed");
console.log("Subset Sum DP verified successfully.");
