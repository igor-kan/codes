/**
 * Broyden-Fletcher-Goldfarb-Shanno (BFGS) Algorithm (Numerical Recipes 3rd Ed. Chapter 10.7)
 * Unconstrained multivariate non-linear optimization with rank-2 inverse Hessian approximation.
 */

function vecAdd(a: number[], b: number[]): number[] {
  return a.map((v, i) => v + b[i]);
}

function vecSub(a: number[], b: number[]): number[] {
  return a.map((v, i) => v - b[i]);
}

function dot(a: number[], b: number[]): number {
  return a.reduce((sum, v, i) => sum + v * b[i], 0);
}

function matVec(A: number[][], v: number[]): number[] {
  return A.map((row) => dot(row, v));
}

export function bfgs(
  f: (x: number[]) => number,
  grad: (x: number[]) => number[],
  x0: number[],
  tol = 1e-6,
  maxIter = 100
): { xmin: number[]; fmin: number } {
  const n = x0.length;
  let x = [...x0];
  let H = Array.from({ length: n }, (_, i) => {
    const row = new Array(n).fill(0);
    row[i] = 1;
    return row;
  });

  let g = grad(x);

  for (let iter = 0; iter < maxIter; iter++) {
    if (Math.sqrt(dot(g, g)) < tol) break;

    const p = matVec(H, g).map((v) => -v);

    // Backtracking line search (Armijo condition)
    let alpha = 1.0;
    const c1 = 1e-4;
    const fx = f(x);
    while (f(vecAdd(x, p.map((v) => alpha * v))) > fx + c1 * alpha * dot(g, p)) {
      alpha *= 0.5;
      if (alpha < 1e-12) break;
    }

    const s = p.map((v) => alpha * v);
    const nextX = vecAdd(x, s);
    const nextG = grad(nextX);
    const y = vecSub(nextG, g);

    const ys = dot(y, s);
    if (ys > 1e-10) {
      // BFGS H update formula
      const Hy = matVec(H, y);
      const yHy = dot(y, Hy);
      for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
          H[i][j] +=
            ((ys + yHy) * s[i] * s[j]) / (ys * ys) -
            (Hy[i] * s[j] + s[i] * Hy[j]) / ys;
        }
      }
    }

    x = nextX;
    g = nextG;
  }
  return { xmin: x, fmin: f(x) };
}

// Rosenbrock function: f(x, y) = (1 - x)^2 + 100(y - x^2)^2
const fRosen = ([x, y]: number[]) => (1 - x) ** 2 + 100 * (y - x * x) ** 2;
const gradRosen = ([x, y]: number[]) => [
  -2 * (1 - x) - 400 * x * (y - x * x),
  200 * (y - x * x),
];

const bfgsRes = bfgs(fRosen, gradRosen, [-1.2, 1.0]);
if (Math.abs(bfgsRes.xmin[0] - 1) > 1e-3 || Math.abs(bfgsRes.xmin[1] - 1) > 1e-3) {
  throw new Error("BFGS Rosenbrock optimization failed");
}
console.log(`NR BFGS Optimization verified: xmin=[${bfgsRes.xmin.map((v) => v.toFixed(4)).join(", ")}]`);
