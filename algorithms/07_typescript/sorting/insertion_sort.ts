export function insertionSort(arr: number[]): number[] {
  const a = arr.slice();
  for (let i = 1; i < a.length; i++) {
    const key = a[i];
    let j = i - 1;
    while (j >= 0 && a[j] > key) { a[j + 1] = a[j]; j--; }
    a[j + 1] = key;
  }
  return a;
}

const sorted = insertionSort([5, 2, 4, 6, 1, 3]);
if (sorted.join(",") !== "1,2,3,4,5,6") throw new Error("Insertion sort failed");
console.log("[TypeScript Insertion Sort] Sorted array verified");
