/**
 * Conjugate Gradient Method for Linear Systems (Numerical Recipes 3rd Ed. Chapter 2.7)
 * Iterative solver for symmetric positive-definite system A x = b in at most n steps.
 */

function dot(a: number[], b: number[]): number {
  return a.reduce((sum, v, i) => sum + v * b[i], 0);
}

function matVec(A: number[][], v: number[]): number[] {
  return A.map((row) => dot(row, v));
}

export function conjugateGradient(
  A: number[][],
  b: number[],
  x0?: number[],
  tol = 1e-10,
  maxIter = 100
): number[] {
  const n = b.length;
  let x = x0 ? [...x0] : new Array(n).fill(0);
  let r = b.map((val, i) => val - dot(A[i], x));
  let p = [...r];
  let rsOld = dot(r, r);

  for (let i = 0; i < maxIter; i++) {
    if (Math.sqrt(rsOld) < tol) break;
    const Ap = matVec(A, p);
    const alpha = rsOld / dot(p, Ap);

    x = x.map((val, idx) => val + alpha * p[idx]);
    r = r.map((val, idx) => val - alpha * Ap[idx]);

    const rsNew = dot(r, r);
    p = r.map((val, idx) => val + (rsNew / rsOld) * p[idx]);
    rsOld = rsNew;
  }
  return x;
}

const cgA = [
  [4, 1],
  [1, 3],
];
const cgB = [1, 2];
const cgX = conjugateGradient(cgA, cgB);
if (Math.abs(cgX[0] - 1 / 11) > 1e-6 || Math.abs(cgX[1] - 7 / 11) > 1e-6) {
  throw new Error("Conjugate Gradient failed");
}
console.log("NR Conjugate Gradient Linear Solver verified successfully.");
