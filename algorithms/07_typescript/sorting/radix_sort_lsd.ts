/**
 * Radix Sort (CLRS 3rd Ed. Chapter 8.3)
 * Non-comparative integer sort running in O(d * (n + k)) time.
 */

export function radixSortLSD(arr: number[]): number[] {
  if (arr.length === 0) return arr;
  const maxVal = Math.max(...arr);

  for (let exp = 1; Math.floor(maxVal / exp) > 0; exp *= 10) {
    countingSortByDigit(arr, exp);
  }
  return arr;
}

function countingSortByDigit(arr: number[], exp: number): void {
  const n = arr.length;
  const output = new Array(n).fill(0);
  const count = new Array(10).fill(0);

  for (let i = 0; i < n; i++) {
    const digit = Math.floor(arr[i] / exp) % 10;
    count[digit]++;
  }

  for (let i = 1; i < 10; i++) {
    count[i] += count[i - 1];
  }

  for (let i = n - 1; i >= 0; i--) {
    const digit = Math.floor(arr[i] / exp) % 10;
    output[count[digit] - 1] = arr[i];
    count[digit]--;
  }

  for (let i = 0; i < n; i++) {
    arr[i] = output[i];
  }
}

const testRS = [170, 45, 75, 90, 802, 24, 2, 66];
radixSortLSD(testRS);
if (testRS.join(",") !== "2,24,45,66,75,90,170,802") throw new Error("Radix Sort failed");
console.log("CLRS Radix Sort verified successfully.");
