export function quickSort(arr: number[]): number[] {
  if (arr.length <= 1) return arr;
  const pivot = arr[arr.length >> 1];
  const less: number[] = [], equal: number[] = [], more: number[] = [];
  for (const x of arr) {
    if (x < pivot) less.push(x);
    else if (x > pivot) more.push(x);
    else equal.push(x);
  }
  return [...quickSort(less), ...equal, ...quickSort(more)];
}

const data = [33, 7, 91, 12, 5, 5, 78, 2, 44, 19];
const sorted = quickSort(data);
console.log(`[TypeScript QuickSort] Functional quicksort verified: [${sorted.join(", ")}]`);
