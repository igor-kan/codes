function lowerBound(arr, target) {
  let lo = 0, hi = arr.length;
  while (lo < hi) {
    const mid = (lo + hi) >> 1;
    if (arr[mid] < target) lo = mid + 1;
    else hi = mid;
  }
  return lo;
}

function upperBound(arr, target) {
  let lo = 0, hi = arr.length;
  while (lo < hi) {
    const mid = (lo + hi) >> 1;
    if (arr[mid] <= target) lo = mid + 1;
    else hi = mid;
  }
  return lo;
}

module.exports = { lowerBound, upperBound };

if (require.main === module) {
  const arr = [1, 3, 3, 3, 5, 7, 9];
  if (lowerBound(arr, 3) !== 1) throw new Error("lowerBound failed");
  if (upperBound(arr, 3) !== 4) throw new Error("upperBound failed");
  if (lowerBound(arr, 4) !== 4) throw new Error("lowerBound insertion failed");
  console.log("[JavaScript Binary Search] lower_bound / upper_bound verified");
}
