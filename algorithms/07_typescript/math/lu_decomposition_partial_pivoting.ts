/**
 * LUP Decomposition with Partial Pivoting (Numerical Recipes 3rd Ed. Chapter 2.3)
 * Factorizes P A = L U for solving general linear systems in O(n^3).
 */

export function lupDecompose(A: number[][]): { LU: number[][]; P: number[]; numSwaps: number } {
  const n = A.length;
  const LU = A.map((row) => [...row]);
  const P = Array.from({ length: n }, (_, i) => i);
  let numSwaps = 0;

  for (let i = 0; i < n; i++) {
    let maxVal = 0;
    let pivot = i;
    for (let k = i; k < n; k++) {
      if (Math.abs(LU[k][i]) > maxVal) {
        maxVal = Math.abs(LU[k][i]);
        pivot = k;
      }
    }
    if (maxVal < 1e-12) throw new Error("Singular matrix");

    if (pivot !== i) {
      [LU[i], LU[pivot]] = [LU[pivot], LU[i]];
      [P[i], P[pivot]] = [P[pivot], P[i]];
      numSwaps++;
    }

    for (let j = i + 1; j < n; j++) {
      LU[j][i] /= LU[i][i];
      for (let k = i + 1; k < n; k++) {
        LU[j][k] -= LU[j][i] * LU[i][k];
      }
    }
  }
  return { LU, P, numSwaps };
}

export function lupSolve(LU: number[][], P: number[], b: number[]): number[] {
  const n = LU.length;
  const x = new Array(n).fill(0);
  const y = new Array(n).fill(0);

  // Forward solve L y = P b
  for (let i = 0; i < n; i++) {
    let sum = 0;
    for (let j = 0; j < i; j++) sum += LU[i][j] * y[j];
    y[i] = b[P[i]] - sum;
  }

  // Back solve U x = y
  for (let i = n - 1; i >= 0; i--) {
    let sum = 0;
    for (let j = i + 1; j < n; j++) sum += LU[i][j] * x[j];
    x[i] = (y[i] - sum) / LU[i][i];
  }
  return x;
}

const luA = [
  [2, 1, -1],
  [-3, -1, 2],
  [-2, 1, 2],
];
const luB = [8, -11, -3];
const { LU, P } = lupDecompose(luA);
const xRes = lupSolve(LU, P, luB);
if (Math.abs(xRes[0] - 2) > 1e-5 || Math.abs(xRes[1] - 3) > 1e-5 || Math.abs(xRes[2] - (-1)) > 1e-5) {
  throw new Error("LUP solver failed");
}
console.log("NR LU Decomposition with Partial Pivoting verified successfully.");
