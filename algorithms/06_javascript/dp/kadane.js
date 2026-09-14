function maxSubarraySum(arr) {
  let best = -Infinity, cur = 0;
  for (const x of arr) {
    cur = Math.max(x, cur + x);
    best = Math.max(best, cur);
  }
  return best;
}

module.exports = { maxSubarraySum };

if (require.main === module) {
  if (maxSubarraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) !== 6) throw new Error("kadane failed");
  if (maxSubarraySum([-1, -2, -3]) !== -1) throw new Error("all-negative case failed");
  console.log("[JavaScript Kadane] Maximum subarray sum verified");
}
