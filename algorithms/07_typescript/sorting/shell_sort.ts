/**
 * Shell Sort (Donald Shell)
 * Generalization of insertion sort with diminishing gaps.
 */

export function shellSort(arr: number[]): number[] {
  const n = arr.length;

  // Knuth gap sequence: h = 3*h + 1
  let h = 1;
  while (h < Math.floor(n / 3)) {
    h = 3 * h + 1;
  }

  while (h >= 1) {
    for (let i = h; i < n; i++) {
      const temp = arr[i];
      let j = i;
      while (j >= h && arr[j - h] > temp) {
        arr[j] = arr[j - h];
        j -= h;
      }
      arr[j] = temp;
    }
    h = Math.floor(h / 3);
  }
  return arr;
}

const testSS = [35, 33, 42, 10, 14, 19, 27, 44];
shellSort(testSS);
if (testSS.join(",") !== "10,14,19,27,33,35,42,44") throw new Error("Shell Sort failed");
console.log("Shell Sort verified successfully.");
