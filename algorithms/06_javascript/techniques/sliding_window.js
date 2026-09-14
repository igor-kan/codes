function maxSumFixedWindow(arr, k) {
  if (k > arr.length) return 0;
  let sum = 0;
  for (let i = 0; i < k; i++) sum += arr[i];
  let max = sum;
  for (let i = k; i < arr.length; i++) {
    sum += arr[i] - arr[i - k];
    if (sum > max) max = sum;
  }
  return max;
}

module.exports = { maxSumFixedWindow };

if (require.main === module) {
  const arr = [1, 4, 2, 10, 23, 3, 1, 0, 20];
  if (maxSumFixedWindow(arr, 4) !== 39) throw new Error("sliding window max sum failed");
  console.log("[JavaScript Sliding Window] Fixed-size max sum verified");
}
