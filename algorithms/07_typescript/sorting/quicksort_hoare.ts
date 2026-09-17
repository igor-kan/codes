/**
 * Hoare's Quicksort Partition (CLRS 3rd Ed. Chapter 7 Problems 7-1)
 * Original partition scheme by C.A.R. Hoare using bidirectional scans.
 */

export function quicksortHoare(arr: number[], low = 0, high = arr.length - 1): number[] {
  if (low < high) {
    const p = hoarePartition(arr, low, high);
    quicksortHoare(arr, low, p);
    quicksortHoare(arr, p + 1, high);
  }
  return arr;
}

function hoarePartition(arr: number[], low: number, high: number): number {
  const pivot = arr[low];
  let i = low - 1;
  let j = high + 1;

  while (true) {
    do {
      i++;
    } while (arr[i] < pivot);

    do {
      j--;
    } while (arr[j] > pivot);

    if (i >= j) return j;
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
}

const testHQ = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11];
quicksortHoare(testHQ);
if (testHQ.join(",") !== "2,4,5,6,7,8,9,11,12,13,19,21") throw new Error("Hoare Quicksort failed");
console.log("Hoare's Quicksort verified successfully.");
