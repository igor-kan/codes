/**
 * Bucket Sort (CLRS 3rd Ed. Chapter 8.4)
 * Linear time average case sorting O(n) for numbers uniformly distributed in [0, 1).
 */

export function bucketSort(arr: number[]): number[] {
  const n = arr.length;
  if (n <= 1) return arr;

  const buckets: number[][] = Array.from({ length: n }, () => []);

  for (let i = 0; i < n; i++) {
    const bucketIndex = Math.min(n - 1, Math.floor(n * arr[i]));
    buckets[bucketIndex].push(arr[i]);
  }

  // Sort each bucket with insertion sort and concatenate
  let idx = 0;
  for (let i = 0; i < n; i++) {
    buckets[i].sort((a, b) => a - b);
    for (const val of buckets[i]) {
      arr[idx++] = val;
    }
  }
  return arr;
}

const testBS = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68];
bucketSort(testBS);
for (let i = 1; i < testBS.length; i++) {
  if (testBS[i] < testBS[i - 1]) throw new Error("Bucket sort failed");
}
console.log("CLRS Bucket Sort verified successfully.");
