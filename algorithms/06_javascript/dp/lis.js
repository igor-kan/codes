function lengthOfLIS(nums) {
  const tails = [];
  for (const x of nums) {
    let lo = 0, hi = tails.length;
    while (lo < hi) {
      const mid = (lo + hi) >> 1;
      if (tails[mid] < x) lo = mid + 1;
      else hi = mid;
    }
    if (lo === tails.length) tails.push(x);
    else tails[lo] = x;
  }
  return tails.length;
}

module.exports = { lengthOfLIS };

if (require.main === module) {
  if (lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) !== 4) throw new Error("LIS failed");
  if (lengthOfLIS([0, 1, 0, 3, 2, 3]) !== 4) throw new Error("LIS failed");
  console.log("[JavaScript LIS] O(n log n) longest increasing subsequence verified");
}
