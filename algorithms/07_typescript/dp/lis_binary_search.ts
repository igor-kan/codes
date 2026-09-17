/**
 * Longest Increasing Subsequence (LIS) in O(n log n)
 * Patience sorting and binary search method to find LIS length and subsequence.
 */

export function lisBinarySearch(arr: number[]): number[] {
  if (arr.length === 0) return [];

  const tails: number[] = [];
  const tailIndices: number[] = [];
  const parent = new Array(arr.length).fill(-1);

  for (let i = 0; i < arr.length; i++) {
    const x = arr[i];
    let l = 0;
    let r = tails.length;

    while (l < r) {
      const mid = (l + r) >> 1;
      if (tails[mid] < x) l = mid + 1;
      else r = mid;
    }

    tails[l] = x;
    tailIndices[l] = i;
    parent[i] = l > 0 ? tailIndices[l - 1] : -1;
  }

  const result: number[] = [];
  let curr = tailIndices[tails.length - 1];
  while (curr !== -1) {
    result.push(arr[curr]);
    curr = parent[curr];
  }
  return result.reverse();
}

const testLIS = [10, 9, 2, 5, 3, 7, 101, 18];
const lisRes = lisBinarySearch(testLIS);
if (lisRes.length !== 4 || lisRes.join(",") !== "2,3,7,18") {
  throw new Error("LIS binary search failed");
}
console.log("LIS O(n log n) verified successfully.");
