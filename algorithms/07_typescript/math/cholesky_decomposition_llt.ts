/**
 * Cholesky Decomposition LL^T (Numerical Recipes 3rd Ed. Chapter 2.6)
 * Factorization of symmetric positive-definite matrix A = L L^T and forward/back substitution.
 */

export function choleskyLLT(A: number[][]): number[][] {
  const n = A.length;
  const L = Array.from({ length: n }, () => new Array(n).fill(0));

  for (let i = 0; i < n; i++) {
    for (let j = 0; j <= i; j++) {
      let sum = 0;
      for (let k = 0; k < j; k++) {
        sum += L[i][k] * L[j][k];
      }

      if (i === j) {
        const val = A[i][i] - sum;
        if (val <= 0) throw new Error("Matrix is not positive definite");
        L[i][j] = Math.sqrt(val);
      } else {
        L[i][j] = (A[i][j] - sum) / L[j][j];
      }
    }
  }
  return L;
}

export function choleskySolve(L: number[][], b: number[]): number[] {
  const n = L.length;
  const y = new Array(n).fill(0);
  // Forward solve L y = b
  for (let i = 0; i < n; i++) {
    let sum = 0;
    for (let j = 0; j < i; j++) sum += L[i][j] * y[j];
    y[i] = (b[i] - sum) / L[i][i];
  }
  // Back solve L^T x = y
  const x = new Array(n).fill(0);
  for (let i = n - 1; i >= 0; i--) {
    let sum = 0;
    for (let j = i + 1; j < n; j++) sum += L[j][i] * x[j];
    x[i] = (y[i] - sum) / L[i][i];
  }
  return x;
}

const spdA = [
  [4, 12, -16],
  [12, 37, -43],
  [-16, -43, 98],
];
const spdB = [1, 2, 3];
const Lmat = choleskyLLT(spdA);
const xSol = choleskySolve(Lmat, spdB);
if (Math.abs(Lmat[0][0] - 2) > 1e-6 || Math.abs(Lmat[1][1] - 1) > 1e-6) {
  throw new Error("Cholesky LL^T failed");
}
console.log("NR Cholesky LL^T verified successfully.");
