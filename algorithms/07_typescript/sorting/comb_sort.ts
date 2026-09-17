/**
 * Comb Sort (Dobosiewicz, Lacey & Box)
 * Improvement over bubble sort using shrink factor 1.3 to eliminate turtles.
 */

export function combSort(arr: number[]): number[] {
  const n = arr.length;
  let gap = n;
  const shrink = 1.3;
  let sorted = false;

  while (!sorted) {
    gap = Math.floor(gap / shrink);
    if (gap <= 1) {
      gap = 1;
      sorted = true;
    }

    for (let i = 0; i + gap < n; i++) {
      if (arr[i] > arr[i + gap]) {
        [arr[i], arr[i + gap]] = [arr[i + gap], arr[i]];
        sorted = false;
      }
    }
  }
  return arr;
}

const testCS = [8, 4, 1, 56, 3, -44, 23, -6, 28, 0];
combSort(testCS);
if (testCS.join(",") !== "-44,-6,0,1,3,4,8,23,28,56") throw new Error("Comb sort failed");
console.log("Comb Sort verified successfully.");
