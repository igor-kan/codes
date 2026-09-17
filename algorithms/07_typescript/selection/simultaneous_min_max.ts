/**
 * Simultaneous Minimum and Maximum (CLRS 3rd Ed. Chapter 9.1)
 * Finds both min and max of n elements using at most 3 * ceil(n / 2) comparisons.
 */

export function findMinMax(arr: number[]): { min: number; max: number } {
  const n = arr.length;
  if (n === 0) throw new Error("Array is empty");

  let min: number;
  let max: number;
  let startIdx = 0;

  if (n % 2 === 1) {
    min = max = arr[0];
    startIdx = 1;
  } else {
    if (arr[0] < arr[1]) {
      min = arr[0];
      max = arr[1];
    } else {
      min = arr[1];
      max = arr[0];
    }
    startIdx = 2;
  }

  for (let i = startIdx; i < n; i += 2) {
    if (arr[i] < arr[i + 1]) {
      if (arr[i] < min) min = arr[i];
      if (arr[i + 1] > max) max = arr[i + 1];
    } else {
      if (arr[i + 1] < min) min = arr[i + 1];
      if (arr[i] > max) max = arr[i];
    }
  }
  return { min, max };
}

const mmRes = findMinMax([18, 4, 25, 2, 7, 9, 33, 1, 12]);
if (mmRes.min !== 1 || mmRes.max !== 33) throw new Error("Simultaneous Min Max failed");
console.log("CLRS Simultaneous Min and Max verified successfully.");
