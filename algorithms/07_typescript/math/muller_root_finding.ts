/**
 * Muller's Method (Numerical Recipes 3rd Ed. Chapter 9.5)
 * Root-finding algorithm using parabolic interpolation capable of locating complex/real roots.
 */

export function mullerRoot(
  f: (x: number) => number,
  p0: number,
  p1: number,
  p2: number,
  tol = 1e-12,
  maxIter = 100
): number {
  for (let i = 0; i < maxIter; i++) {
    const f0 = f(p0), f1 = f(p1), f2 = f(p2);
    const h1 = p1 - p0;
    const h2 = p2 - p1;
    const delta1 = (f1 - f0) / h1;
    const delta2 = (f2 - f1) / h2;
    const d = (delta2 - delta1) / (h2 + h1);

    const b = delta2 + h2 * d;
    const discr = Math.sqrt(Math.max(0, b * b - 4 * f2 * d));

    const denom = Math.abs(b - discr) > Math.abs(b + discr) ? b - discr : b + discr;
    if (denom === 0) return p2;

    const p3 = p2 - (2 * f2) / denom;
    if (Math.abs(p3 - p2) < tol || Math.abs(f(p3)) < tol) return p3;

    p0 = p1;
    p1 = p2;
    p2 = p3;
  }
  return p2;
}

const mRoot = mullerRoot((x) => x * x * x - 13 * x - 12, 4.5, 5.5, 5.0);
if (Math.abs(mRoot - 4) > 1e-6) throw new Error("Muller's method failed");
console.log(`NR Muller's Method verified: root=${mRoot}`);
