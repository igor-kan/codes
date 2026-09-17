/**
 * TimSort Implementation (Tim Peters)
 * Hybrid stable sorting algorithm derived from merge sort and insertion sort.
 */

const RUN = 32;

function insertionSortRange(arr: number[], left: number, right: number): void {
  for (let i = left + 1; i <= right; i++) {
    const temp = arr[i];
    let j = i - 1;
    while (j >= left && arr[j] > temp) {
      arr[j + 1] = arr[j];
      j--;
    }
    arr[j + 1] = temp;
  }
}

function mergeRanges(arr: number[], l: number, m: number, r: number): void {
  const left = arr.slice(l, m + 1);
  const right = arr.slice(m + 1, r + 1);

  let i = 0, j = 0, k = l;
  while (i < left.length && j < right.length) {
    if (left[i] <= right[j]) arr[k++] = left[i++];
    else arr[k++] = right[j++];
  }
  while (i < left.length) arr[k++] = left[i++];
  while (j < right.length) arr[k++] = right[j++];
}

export function timSort(arr: number[]): number[] {
  const n = arr.length;
  for (let i = 0; i < n; i += RUN) {
    insertionSortRange(arr, i, Math.min(i + RUN - 1, n - 1));
  }

  for (let size = RUN; size < n; size = 2 * size) {
    for (let left = 0; left < n; left += 2 * size) {
      const mid = left + size - 1;
      const right = Math.min(left + 2 * size - 1, n - 1);
      if (mid < right) mergeRanges(arr, left, mid, right);
    }
  }
  return arr;
}

const testTS = [5, 21, -3, 45, 0, 12, 100, 2, 8, 4, 3, 9, -1, 10];
timSort(testTS);
for (let i = 1; i < testTS.length; i++) {
  if (testTS[i] < testTS[i - 1]) throw new Error("TimSort failed");
}
console.log("TimSort verified successfully.");
