/**
 * Median of Medians Algorithm (CLRS 3rd Ed. Chapter 9.3)
 * Worst-case deterministic O(n) selection algorithm (Blum, Floyd, Pratt, Rivest, Tarjan).
 */

export function selectMedianOfMedians(arr: number[], k: number): number {
  if (arr.length <= 5) {
    arr.sort((a, b) => a - b);
    return arr[k];
  }

  // Divide into groups of 5 and find medians
  const medians: number[] = [];
  for (let i = 0; i < arr.length; i += 5) {
    const group = arr.slice(i, Math.min(i + 5, arr.length));
    group.sort((a, b) => a - b);
    medians.push(group[Math.floor(group.length / 2)]);
  }

  const pivot = selectMedianOfMedians(medians, Math.floor(medians.length / 2));

  const lows: number[] = [];
  const highs: number[] = [];
  const pivots: number[] = [];

  for (const x of arr) {
    if (x < pivot) lows.push(x);
    else if (x > pivot) highs.push(x);
    else pivots.push(x);
  }

  if (k < lows.length) {
    return selectMedianOfMedians(lows, k);
  } else if (k < lows.length + pivots.length) {
    return pivot;
  } else {
    return selectMedianOfMedians(highs, k - lows.length - pivots.length);
  }
}

const testMM = [12, 3, 5, 7, 4, 19, 26, 1, 14, 8, 22];
const resK3 = selectMedianOfMedians(testMM, 3); // 4th smallest
if (resK3 !== 5) throw new Error("Median of Medians failed");
console.log("CLRS Median of Medians verified successfully.");
