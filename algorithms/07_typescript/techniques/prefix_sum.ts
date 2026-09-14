export function prefixSum(arr: number[]): number[] {
  const pref = new Array(arr.length + 1).fill(0);
  for (let i = 0; i < arr.length; i++) pref[i + 1] = pref[i] + arr[i];
  return pref;
}

export function rangeSum(pref: number[], l: number, r: number): number {
  return pref[r + 1] - pref[l];
}

const pref = prefixSum([3, 1, 4, 1, 5, 9]);
if (rangeSum(pref, 1, 3) !== 6 || rangeSum(pref, 0, 5) !== 23) throw new Error("Prefix sum failed");
console.log("[TypeScript Prefix Sum] 1-indexed prefix sums verified");
