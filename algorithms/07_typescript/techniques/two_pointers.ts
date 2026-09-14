export function twoSumSorted(arr: number[], target: number): number[] {
  let l = 0, r = arr.length - 1;
  while (l < r) {
    const sum = arr[l] + arr[r];
    if (sum === target) return [l, r];
    if (sum < target) l++;
    else r--;
  }
  return [-1, -1];
}

const arr = [2, 7, 11, 15];
const [i, j] = twoSumSorted(arr, 9);
if (i === -1 || arr[i] + arr[j] !== 9) throw new Error("Two pointers failed");
console.log("[TypeScript Two Pointers] Sorted two-sum verified");
