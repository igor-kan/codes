function prefixSum(arr) {
  const pref = new Array(arr.length + 1).fill(0);
  for (let i = 0; i < arr.length; i++) pref[i + 1] = pref[i] + arr[i];
  return pref;
}

function rangeSum(pref, l, r) {
  return pref[r + 1] - pref[l];
}

module.exports = { prefixSum, rangeSum };

if (require.main === module) {
  const pref = prefixSum([3, 1, 4, 1, 5, 9]);
  if (rangeSum(pref, 1, 3) !== 6) throw new Error("prefix range sum failed");
  if (rangeSum(pref, 0, 5) !== 23) throw new Error("full range sum failed");
  console.log("[JavaScript Prefix Sum] 1-indexed prefix sums verified");
}
