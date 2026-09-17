/**
 * Burrows-Wheeler Transform (BWT)
 * Block-sorting data compression transformation and exact inverse reconstruction.
 */

export function bwtEncode(s: string): { transformed: string; originalIndex: number } {
  const n = s.length;
  const rotations: string[] = [];
  for (let i = 0; i < n; i++) {
    rotations.push(s.slice(i) + s.slice(0, i));
  }
  rotations.sort();

  let transformed = "";
  let originalIndex = -1;
  for (let i = 0; i < n; i++) {
    transformed += rotations[i][n - 1];
    if (rotations[i] === s) originalIndex = i;
  }
  return { transformed, originalIndex };
}

export function bwtDecode(transformed: string, originalIndex: number): string {
  const n = transformed.length;
  const table: string[] = new Array(n).fill("");

  for (let iter = 0; iter < n; iter++) {
    for (let i = 0; i < n; i++) {
      table[i] = transformed[i] + table[i];
    }
    table.sort();
  }
  return table[originalIndex];
}

const original = "banana$";
const { transformed, originalIndex } = bwtEncode(original);
const recovered = bwtDecode(transformed, originalIndex);
if (recovered !== original) throw new Error("BWT failed");
console.log("Burrows-Wheeler Transform verified successfully.");
