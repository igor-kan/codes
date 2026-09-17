/**
 * Halley's Method (Numerical Recipes 3rd Ed. Chapter 9.4)
 * Third-order Householder method with cubic rate of convergence using f, f', and f''.
 */

export function halleyRoot(
  f: (x: number) => number,
  df: (x: number) => number,
  d2f: (x: number) => number,
  x0: number,
  tol = 1e-12,
  maxIter = 100
): number {
  let x = x0;
  for (let i = 0; i < maxIter; i++) {
    const y = f(x);
    if (Math.abs(y) < tol) return x;
    const yPrime = df(x);
    const yPrime2 = d2f(x);

    const step = (2 * y * yPrime) / (2 * yPrime * yPrime - y * yPrime2);
    x -= step;
    if (Math.abs(step) < tol) return x;
  }
  return x;
}

// f(x) = x^2 - 2, f'(x) = 2x, f''(x) = 2
const sqrt2 = halleyRoot((x) => x * x - 2, (x) => 2 * x, () => 2, 1.0);
if (Math.abs(sqrt2 - Math.SQRT2) > 1e-12) throw new Error("Halley's method failed");
console.log(`NR Halley's Method verified: sqrt2=${sqrt2}`);
