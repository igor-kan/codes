/**
 * Matrix Chain Multiplication (CLRS 3rd Ed. Chapter 15.2)
 * Computes optimal parenthesization of a chain of matrices to minimize scalar multiplications.
 */

export function matrixChainOrder(p: number[]): { m: number[][]; s: number[][]; minOps: number } {
  const n = p.length - 1;
  const m = Array.from({ length: n + 1 }, () => new Array(n + 1).fill(0));
  const s = Array.from({ length: n + 1 }, () => new Array(n + 1).fill(0));

  for (let l = 2; l <= n; l++) {
    for (let i = 1; i <= n - l + 1; i++) {
      const j = i + l - 1;
      m[i][j] = Infinity;
      for (let k = i; k <= j - 1; k++) {
        const q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j];
        if (q < m[i][j]) {
          m[i][j] = q;
          s[i][j] = k;
        }
      }
    }
  }
  return { m, s, minOps: m[1][n] };
}

export function printOptimalParens(s: number[][], i: number, j: number): string {
  if (i === j) return `A${i}`;
  return `(${printOptimalParens(s, i, s[i][j])}${printOptimalParens(s, s[i][j] + 1, j)})`;
}

const dims = [30, 35, 15, 5, 10, 20, 25];
const mcRes = matrixChainOrder(dims);
if (mcRes.minOps !== 15125) throw new Error("Matrix Chain Order failed");
const parens = printOptimalParens(mcRes.s, 1, 6);
console.log(`CLRS Matrix Chain verified: ops=${mcRes.minOps}, parens=${parens}`);
