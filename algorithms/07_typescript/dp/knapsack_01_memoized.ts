/**
 * 0/1 Knapsack Problem with Backtracking Reconstruction
 * Selects subset of items maximizing value without exceeding capacity W.
 */

export interface KnapsackItem {
  weight: number;
  value: number;
  id?: string | number;
}

export function knapsack01(
  items: KnapsackItem[],
  capacity: number
): { maxValue: number; selectedIndices: number[] } {
  const n = items.length;
  const dp = Array.from({ length: n + 1 }, () => new Array(capacity + 1).fill(0));

  for (let i = 1; i <= n; i++) {
    const { weight, value } = items[i - 1];
    for (let w = 0; w <= capacity; w++) {
      if (weight <= w) {
        dp[i][w] = Math.max(dp[i - 1][w], dp[i - 1][w - weight] + value);
      } else {
        dp[i][w] = dp[i - 1][w];
      }
    }
  }

  const selectedIndices: number[] = [];
  let curW = capacity;
  for (let i = n; i > 0; i--) {
    if (dp[i][curW] !== dp[i - 1][curW]) {
      selectedIndices.push(i - 1);
      curW -= items[i - 1].weight;
    }
  }
  return { maxValue: dp[n][capacity], selectedIndices: selectedIndices.reverse() };
}

const items: KnapsackItem[] = [
  { weight: 2, value: 3 },
  { weight: 3, value: 4 },
  { weight: 4, value: 5 },
  { weight: 5, value: 8 },
];
const kpRes = knapsack01(items, 5);
if (kpRes.maxValue !== 8) throw new Error("0/1 Knapsack failed");
console.log("0/1 Knapsack verified successfully.");
