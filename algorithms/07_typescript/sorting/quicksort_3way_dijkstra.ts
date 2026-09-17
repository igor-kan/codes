/**
 * 3-Way Partition Quicksort (Dutch National Flag problem / Dijkstra)
 * Efficiently handles inputs with high frequencies of identical keys in O(n) time.
 */

export function quicksort3Way(arr: number[], low = 0, high = arr.length - 1): number[] {
  if (low >= high) return arr;

  let lt = low;
  let gt = high;
  const pivot = arr[low];
  let i = low + 1;

  while (i <= gt) {
    if (arr[i] < pivot) {
      [arr[lt], arr[i]] = [arr[i], arr[lt]];
      lt++;
      i++;
    } else if (arr[i] > pivot) {
      [arr[i], arr[gt]] = [arr[gt], arr[i]];
      gt--;
    } else {
      i++;
    }
  }

  quicksort3Way(arr, low, lt - 1);
  quicksort3Way(arr, gt + 1, high);
  return arr;
}

const test3W = [4, 2, 4, 3, 4, 1, 4, 2, 3];
quicksort3Way(test3W);
if (test3W.join(",") !== "1,2,2,3,3,4,4,4,4") throw new Error("3-Way Quicksort failed");
console.log("3-Way Quicksort verified successfully.");
