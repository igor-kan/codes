/**
 * Romberg Integration (Numerical Recipes 3rd Ed. Chapter 4.3)
 * Composite trapezoid rule combined with Richardson extrapolation in O(2^k).
 */

export function rombergIntegrate(
  f: (x: number) => number,
  a: number,
  b: number,
  maxOrder = 5,
  tol = 1e-10
): number {
  const R: number[][] = Array.from({ length: maxOrder }, () => new Array(maxOrder).fill(0));

  // R[0][0] = trapezoid with 1 interval
  R[0][0] = 0.5 * (b - a) * (f(a) + f(b));

  for (let i = 1; i < maxOrder; i++) {
    const n = 1 << i;
    const h = (b - a) / n;
    let sum = 0;
    for (let k = 1; k < n; k += 2) {
      sum += f(a + k * h);
    }
    R[i][0] = 0.5 * R[i - 1][0] + h * sum;

    for (let j = 1; j <= i; j++) {
      R[i][j] = R[i][j - 1] + (R[i][j - 1] - R[i - 1][j - 1]) / (4 ** j - 1);
    }

    if (Math.abs(R[i][i] - R[i - 1][i - 1]) < tol) {
      return R[i][i];
    }
  }
  return R[maxOrder - 1][maxOrder - 1];
}

// Integral of sin(x) from 0 to pi = 2
const rombRes = rombergIntegrate(Math.sin, 0, Math.PI, 6);
if (Math.abs(rombRes - 2.0) > 1e-8) throw new Error("Romberg integration failed");
console.log(`NR Romberg Integration verified: result=${rombRes}`);
