/**
 * Square-Root-Free Cholesky Decomposition A = L D L^T (Numerical Recipes 3rd Ed. Chapter 2.6)
 * Avoids square roots; applicable to symmetric positive-definite and indefinite matrices.
 */

export function choleskyLDLT(A: number[][]): { L: number[][]; D: number[] } {
  const n = A.length;
  const L = Array.from({ length: n }, (_, i) => {
    const row = new Array(n).fill(0);
    row[i] = 1;
    return row;
  });
  const D = new Array(n).fill(0);

  for (let i = 0; i < n; i++) {
    let sumD = 0;
    for (let k = 0; k < i; k++) {
      sumD += L[i][k] * L[i][k] * D[k];
    }
    D[i] = A[i][i] - sumD;
    if (Math.abs(D[i]) < 1e-12) throw new Error("Zero pivot encountered");

    for (let j = i + 1; j < n; j++) {
      let sumL = 0;
      for (let k = 0; k < i; k++) {
        sumL += L[j][k] * L[i][k] * D[k];
      }
      L[j][i] = (A[j][i] - sumL) / D[i];
    }
  }
  return { L, D };
}

const ldltA = [
  [4, 12, -16],
  [12, 37, -43],
  [-16, -43, 98],
];
const { L: lMat, D: dVec } = choleskyLDLT(ldltA);
if (dVec[0] !== 4 || dVec[1] !== 1) throw new Error("Cholesky LDL^T failed");
console.log("NR Cholesky LDL^T verified successfully.");
