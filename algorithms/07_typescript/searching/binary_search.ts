export function lowerBound(arr: number[], target: number): number {
  let lo = 0, hi = arr.length;
  while (lo < hi) {
    const mid = (lo + hi) >> 1;
    if (arr[mid] < target) lo = mid + 1;
    else hi = mid;
  }
  return lo;
}

export function upperBound(arr: number[], target: number): number {
  let lo = 0, hi = arr.length;
  while (lo < hi) {
    const mid = (lo + hi) >> 1;
    if (arr[mid] <= target) lo = mid + 1;
    else hi = mid;
  }
  return lo;
}

const arr = [1, 3, 3, 3, 5, 7, 9];
if (lowerBound(arr, 3) !== 1 || upperBound(arr, 3) !== 4) throw new Error("Binary search bounds failed");
console.log("[TypeScript Binary Search] lower_bound / upper_bound verified");
