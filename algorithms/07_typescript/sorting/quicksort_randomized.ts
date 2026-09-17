/**
 * Randomized Quicksort (CLRS 3rd Ed. Chapter 7.3)
 * Eliminates worst-case O(n^2) on sorted inputs by randomizing pivot selection.
 */

export function randomizedQuicksort(arr: number[], low = 0, high = arr.length - 1): number[] {
  if (low < high) {
    const p = randomizedPartition(arr, low, high);
    randomizedQuicksort(arr, low, p - 1);
    randomizedQuicksort(arr, p + 1, high);
  }
  return arr;
}

function randomizedPartition(arr: number[], low: number, high: number): number {
  const randomIdx = low + Math.floor(Math.random() * (high - low + 1));
  [arr[randomIdx], arr[high]] = [arr[high], arr[randomIdx]];

  const pivot = arr[high];
  let i = low - 1;
  for (let j = low; j < high; j++) {
    if (arr[j] <= pivot) {
      i++;
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
  }
  [arr[i + 1], arr[high]] = [arr[high], arr[i + 1]];
  return i + 1;
}

const testRQ = [10, 7, 8, 9, 1, 5];
randomizedQuicksort(testRQ);
if (testRQ.join(",") !== "1,5,7,8,9,10") throw new Error("Randomized Quicksort failed");
console.log("CLRS Randomized Quicksort verified successfully.");
