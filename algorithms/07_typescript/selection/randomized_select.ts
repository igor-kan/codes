/**
 * Randomized-Select Algorithm (CLRS 3rd Ed. Chapter 9.2)
 * Expected linear-time algorithm to find the i-th smallest element.
 */

export function randomizedSelect(arr: number[], p: number, r: number, i: number): number {
  if (p === r) return arr[p];
  const q = randomizedPartition(arr, p, r);
  const k = q - p + 1;

  if (i === k) return arr[q];
  else if (i < k) return randomizedSelect(arr, p, q - 1, i);
  else return randomizedSelect(arr, q + 1, r, i - k);
}

function randomizedPartition(arr: number[], p: number, r: number): number {
  const rand = p + Math.floor(Math.random() * (r - p + 1));
  [arr[rand], arr[r]] = [arr[r], arr[rand]];
  const pivot = arr[r];
  let idx = p - 1;

  for (let j = p; j < r; j++) {
    if (arr[j] <= pivot) {
      idx++;
      [arr[idx], arr[j]] = [arr[j], arr[idx]];
    }
  }
  [arr[idx + 1], arr[r]] = [arr[r], arr[idx + 1]];
  return idx + 1;
}

const testRSel = [6, 1, 9, 3, 7, 2, 8];
const thirdSmallest = randomizedSelect(testRSel, 0, testRSel.length - 1, 3);
if (thirdSmallest !== 3) throw new Error("Randomized Select failed");
console.log("CLRS Randomized Select verified successfully.");
