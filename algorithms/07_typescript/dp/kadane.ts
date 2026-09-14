export function maxSubarraySum(arr: number[]): number {
  let best = -Infinity, cur = 0;
  for (const x of arr) {
    cur = Math.max(x, cur + x);
    best = Math.max(best, cur);
  }
  return best;
}

if (maxSubarraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) !== 6) throw new Error("Kadane failed");
console.log("[TypeScript Kadane] Maximum subarray sum verified");
