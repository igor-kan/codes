/**
 * K-th Element of Two Sorted Arrays
 * Binary search partition finding k-th element in O(log(min(m, n))) time.
 */

export function findKthElement(a: number[], b: number[], k: number): number {
  if (a.length > b.length) return findKthElement(b, a, k);

  const m = a.length;
  const n = b.length;
  let low = Math.max(0, k - n);
  let high = Math.min(m, k);

  while (low <= high) {
    const cutA = (low + high) >> 1;
    const cutB = k - cutA;

    const leftA = cutA === 0 ? -Infinity : a[cutA - 1];
    const leftB = cutB === 0 ? -Infinity : b[cutB - 1];
    const rightA = cutA === m ? Infinity : a[cutA];
    const rightB = cutB === n ? Infinity : b[cutB];

    if (leftA <= rightB && leftB <= rightA) {
      return Math.max(leftA, leftB);
    } else if (leftA > rightB) {
      high = cutA - 1;
    } else {
      low = cutA + 1;
    }
  }
  throw new Error("Invalid input");
}

const arr1 = [2, 3, 6, 7, 9];
const arr2 = [1, 4, 8, 10];
const kVal = findKthElement(arr1, arr2, 5); // 5th element in merged: [1,2,3,4,6,...] -> 6
if (kVal !== 6) throw new Error("K-th element of two sorted arrays failed");
console.log("K-th Element of Two Sorted Arrays verified successfully.");
