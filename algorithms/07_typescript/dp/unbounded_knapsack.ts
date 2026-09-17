/**
 * Unbounded Knapsack Problem
 * Finds combination of items with infinite supplies maximizing value within capacity W in O(nW).
 */

export function unboundedKnapsack(weights: number[], values: number[], capacity: number): number {
  const dp = new Array(capacity + 1).fill(0);

  for (let w = 1; w <= capacity; w++) {
    for (let i = 0; i < weights.length; i++) {
      if (weights[i] <= w) {
        dp[w] = Math.max(dp[w], dp[w - weights[i]] + values[i]);
      }
    }
  }
  return dp[capacity];
}

const uRes = unboundedKnapsack([1, 3, 4, 5], [10, 40, 50, 70], 8);
if (uRes !== 110) throw new Error("Unbounded Knapsack failed");
console.log("Unbounded Knapsack verified successfully.");
