/**
 * Simplex Algorithm for Linear Programming (CLRS 3rd Ed. Chapter 29)
 * Standard form maximization: maximize c^T x subject to Ax <= b and x >= 0.
 */

export function simplex(
  A: number[][], // m x n
  b: number[],   // m
  c: number[]    // n
): { optimalValue: number; solution: number[] } {
  const m = A.length;
  const n = c.length;

  // Tableau has m + 1 rows, n + m + 1 cols
  const T = Array.from({ length: m + 1 }, () => new Array(n + m + 1).fill(0));

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) T[i][j] = A[i][j];
    T[i][n + i] = 1; // slack variable
    T[i][n + m] = b[i];
  }

  for (let j = 0; j < n; j++) T[m][j] = -c[j];

  const basis = Array.from({ length: m }, (_, i) => n + i);

  while (true) {
    // Find entering variable (most negative in bottom row)
    let q = -1;
    for (let j = 0; j < n + m; j++) {
      if (T[m][j] < (q === -1 ? 0 : T[m][q])) q = j;
    }
    if (q === -1 || T[m][q] >= 0) break; // Optimal reached

    // Find leaving variable (min ratio test)
    let p = -1;
    for (let i = 0; i < m; i++) {
      if (T[i][q] > 0) {
        if (p === -1 || T[i][n + m] / T[i][q] < T[p][n + m] / T[p][q]) {
          p = i;
        }
      }
    }
    if (p === -1) throw new Error("Linear program is unbounded");

    // Pivot on (p, q)
    const pivot = T[p][q];
    for (let j = 0; j <= n + m; j++) T[p][j] /= pivot;

    for (let i = 0; i <= m; i++) {
      if (i !== p && Math.abs(T[i][q]) > 1e-12) {
        const factor = T[i][q];
        for (let j = 0; j <= n + m; j++) {
          T[i][j] -= factor * T[p][j];
        }
      }
    }
    basis[p] = q;
  }

  const solution = new Array(n).fill(0);
  for (let i = 0; i < m; i++) {
    if (basis[i] < n) solution[basis[i]] = T[i][n + m];
  }
  return { optimalValue: T[m][n + m], solution };
}

// Maximize 3x1 + 2x2 subject to 2x1 + x2 <= 100, x1 + x2 <= 80, x1 <= 40
const lpA = [
  [2, 1],
  [1, 1],
  [1, 0],
];
const lpB = [100, 80, 40];
const lpC = [3, 2];
const lpRes = simplex(lpA, lpB, lpC);
if (Math.abs(lpRes.optimalValue - 180) > 1e-4) throw new Error("Simplex LP failed");
console.log("CLRS Simplex Linear Programming verified successfully.");
