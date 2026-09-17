/**
 * Heap Sort (CLRS 3rd Ed. Chapter 6)
 * In-place sorting algorithm with guaranteed O(n log n) running time.
 */

export function heapSort(arr: number[]): number[] {
  const n = arr.length;

  function maxHeapify(i: number, size: number): void {
    let largest = i;
    const l = 2 * i + 1;
    const r = 2 * i + 2;

    if (l < size && arr[l] > arr[largest]) largest = l;
    if (r < size && arr[r] > arr[largest]) largest = r;

    if (largest !== i) {
      [arr[i], arr[largest]] = [arr[largest], arr[i]];
      maxHeapify(largest, size);
    }
  }

  // Build max heap
  for (let i = Math.floor(n / 2) - 1; i >= 0; i--) {
    maxHeapify(i, n);
  }

  // Extract elements from heap
  for (let i = n - 1; i > 0; i--) {
    [arr[0], arr[i]] = [arr[i], arr[0]];
    maxHeapify(0, i);
  }

  return arr;
}

const testH = [12, 11, 13, 5, 6, 7];
heapSort(testH);
if (testH.join(",") !== "5,6,7,11,12,13") throw new Error("HeapSort failed");
console.log("CLRS Heap Sort verified successfully.");
