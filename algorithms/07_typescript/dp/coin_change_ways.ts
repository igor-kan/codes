/**
 * Coin Change Dynamic Programming
 * Computes both total distinct combinations and minimal coins to achieve amount.
 */

export function coinChangeWays(coins: number[], amount: number): number {
  const dp = new Array(amount + 1).fill(0);
  dp[0] = 1;
  for (const c of coins) {
    for (let a = c; a <= amount; a++) {
      dp[a] += dp[a - c];
    }
  }
  return dp[amount];
}

export function coinChangeMin(coins: number[], amount: number): number {
  const dp = new Array(amount + 1).fill(Infinity);
  dp[0] = 0;
  for (let a = 1; a <= amount; a++) {
    for (const c of coins) {
      if (c <= a && dp[a - c] !== Infinity) {
        dp[a] = Math.min(dp[a], dp[a - c] + 1);
      }
    }
  }
  return dp[amount] === Infinity ? -1 : dp[amount];
}

if (coinChangeWays([1, 2, 5], 5) !== 4 || coinChangeMin([1, 2, 5], 11) !== 3) {
  throw new Error("Coin Change failed");
}
console.log("Coin Change verified successfully.");
